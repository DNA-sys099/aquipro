import React, { useState } from 'react';
import { styled } from '@mui/material/styles';
import {
  Box,
  Paper,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  TablePagination,
  Typography,
  Button,
  Chip,
  IconButton,
  TextField,
  InputAdornment,
} from '@mui/material';
import SearchIcon from '@mui/icons-material/Search';
import AddIcon from '@mui/icons-material/Add';
import MoreVertIcon from '@mui/icons-material/MoreVert';
import { motion } from 'framer-motion';

const StyledPaper = styled(Paper)(({ theme }) => ({
  padding: theme.spacing(3),
  borderRadius: theme.shape.borderRadius * 2,
  background: `linear-gradient(45deg, ${theme.palette.background.paper} 0%, ${theme.palette.background.paper} 100%)`,
  boxShadow: '0 8px 32px 0 rgba(31, 38, 135, 0.37)',
  backdropFilter: 'blur(4px)',
  border: '1px solid rgba(255, 255, 255, 0.18)',
}));

const StyledTableCell = styled(TableCell)(({ theme }) => ({
  borderBottom: '1px solid rgba(255, 255, 255, 0.12)',
}));

const StatusChip = styled(Chip)(({ theme, status }) => {
  const getColor = () => {
    switch (status) {
      case 'Active':
        return theme.palette.success;
      case 'Pending':
        return theme.palette.warning;
      case 'Inactive':
        return theme.palette.error;
      default:
        return theme.palette.primary;
    }
  };

  return {
    backgroundColor: getColor().main + '20',
    color: getColor().main,
    '& .MuiChip-label': {
      fontWeight: 600,
    },
  };
});

const clients = [
  {
    id: 1,
    name: 'Acme Corporation',
    contact: 'John Smith',
    email: 'john@acme.com',
    status: 'Active',
    revenue: '$15,000',
    startDate: '2024-01-15',
  },
  {
    id: 2,
    name: 'Tech Innovators',
    contact: 'Sarah Johnson',
    email: 'sarah@techinnovators.com',
    status: 'Pending',
    revenue: '$8,500',
    startDate: '2024-01-20',
  },
  {
    id: 3,
    name: 'Global Solutions',
    contact: 'Mike Wilson',
    email: 'mike@globalsolutions.com',
    status: 'Active',
    revenue: '$12,000',
    startDate: '2024-01-10',
  },
  {
    id: 4,
    name: 'Digital Ventures',
    contact: 'Emily Brown',
    email: 'emily@digitalventures.com',
    status: 'Inactive',
    revenue: '$5,000',
    startDate: '2023-12-15',
  },
  {
    id: 5,
    name: 'Future Systems',
    contact: 'David Lee',
    email: 'david@futuresystems.com',
    status: 'Active',
    revenue: '$20,000',
    startDate: '2024-01-05',
  },
];

const Clients = () => {
  const [page, setPage] = useState(0);
  const [rowsPerPage, setRowsPerPage] = useState(5);
  const [searchTerm, setSearchTerm] = useState('');

  const handleChangePage = (event, newPage) => {
    setPage(newPage);
  };

  const handleChangeRowsPerPage = (event) => {
    setRowsPerPage(parseInt(event.target.value, 10));
    setPage(0);
  };

  const filteredClients = clients.filter((client) =>
    Object.values(client).some(
      (value) =>
        value.toString().toLowerCase().includes(searchTerm.toLowerCase())
    )
  );

  return (
    <Box>
      <Box sx={{ display: 'flex', justifyContent: 'space-between', mb: 4 }}>
        <Typography variant="h4">Clients</Typography>
        <Button
          variant="contained"
          startIcon={<AddIcon />}
          sx={{
            borderRadius: 2,
            px: 3,
          }}
        >
          Add Client
        </Button>
      </Box>

      <StyledPaper
        component={motion.div}
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
      >
        <Box sx={{ mb: 3 }}>
          <TextField
            fullWidth
            variant="outlined"
            placeholder="Search clients..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            InputProps={{
              startAdornment: (
                <InputAdornment position="start">
                  <SearchIcon />
                </InputAdornment>
              ),
            }}
            sx={{
              '& .MuiOutlinedInput-root': {
                borderRadius: 2,
              },
            }}
          />
        </Box>

        <TableContainer>
          <Table>
            <TableHead>
              <TableRow>
                <StyledTableCell>Client Name</StyledTableCell>
                <StyledTableCell>Contact</StyledTableCell>
                <StyledTableCell>Email</StyledTableCell>
                <StyledTableCell>Status</StyledTableCell>
                <StyledTableCell>Revenue</StyledTableCell>
                <StyledTableCell>Start Date</StyledTableCell>
                <StyledTableCell align="right">Actions</StyledTableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {filteredClients
                .slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage)
                .map((client) => (
                  <TableRow
                    key={client.id}
                    component={motion.tr}
                    whileHover={{ backgroundColor: 'rgba(255, 255, 255, 0.05)' }}
                  >
                    <StyledTableCell>{client.name}</StyledTableCell>
                    <StyledTableCell>{client.contact}</StyledTableCell>
                    <StyledTableCell>{client.email}</StyledTableCell>
                    <StyledTableCell>
                      <StatusChip
                        label={client.status}
                        status={client.status}
                        size="small"
                      />
                    </StyledTableCell>
                    <StyledTableCell>{client.revenue}</StyledTableCell>
                    <StyledTableCell>{client.startDate}</StyledTableCell>
                    <StyledTableCell align="right">
                      <IconButton size="small">
                        <MoreVertIcon />
                      </IconButton>
                    </StyledTableCell>
                  </TableRow>
                ))}
            </TableBody>
          </Table>
        </TableContainer>

        <TablePagination
          component="div"
          count={filteredClients.length}
          page={page}
          onPageChange={handleChangePage}
          rowsPerPage={rowsPerPage}
          onRowsPerPageChange={handleChangeRowsPerPage}
          sx={{
            borderTop: '1px solid rgba(255, 255, 255, 0.12)',
          }}
        />
      </StyledPaper>
    </Box>
  );
};

export default Clients;
