import React from 'react';
import { styled } from '@mui/material/styles';
import {
  Box,
  Paper,
  Typography,
  Button,
  Chip,
  Avatar,
  IconButton,
} from '@mui/material';
import AddIcon from '@mui/icons-material/Add';
import MoreVertIcon from '@mui/icons-material/MoreVert';
import { motion, Reorder } from 'framer-motion';

const StyledPaper = styled(Paper)(({ theme }) => ({
  padding: theme.spacing(3),
  borderRadius: theme.shape.borderRadius * 2,
  background: `linear-gradient(45deg, ${theme.palette.background.paper} 0%, ${theme.palette.background.paper} 100%)`,
  boxShadow: '0 8px 32px 0 rgba(31, 38, 135, 0.37)',
  backdropFilter: 'blur(4px)',
  border: '1px solid rgba(255, 255, 255, 0.18)',
}));

const KanbanColumn = styled(StyledPaper)(({ theme }) => ({
  height: 'calc(100vh - 200px)',
  overflowY: 'auto',
  minWidth: 300,
  margin: theme.spacing(1),
}));

const TaskCard = styled(motion(Paper))(({ theme }) => ({
  padding: theme.spacing(2),
  marginBottom: theme.spacing(2),
  borderRadius: theme.shape.borderRadius,
  backgroundColor: theme.palette.background.default,
  border: '1px solid rgba(255, 255, 255, 0.12)',
  cursor: 'grab',
  '&:active': {
    cursor: 'grabbing',
  },
}));

const PriorityChip = styled(Chip)(({ theme, priority }) => {
  const getColor = () => {
    switch (priority) {
      case 'High':
        return theme.palette.error;
      case 'Medium':
        return theme.palette.warning;
      case 'Low':
        return theme.palette.success;
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

const tasks = {
  todo: [
    {
      id: 1,
      title: 'Client Onboarding',
      description: 'Complete onboarding process for new client XYZ Corp',
      priority: 'High',
      assignee: 'JS',
      dueDate: '2024-02-15',
    },
    {
      id: 2,
      title: 'Content Strategy',
      description: 'Develop Q1 content strategy for Tech Innovators',
      priority: 'Medium',
      assignee: 'AK',
      dueDate: '2024-02-20',
    },
  ],
  inProgress: [
    {
      id: 3,
      title: 'Campaign Analysis',
      description: 'Analyze Q4 campaign performance and prepare report',
      priority: 'High',
      assignee: 'ML',
      dueDate: '2024-02-10',
    },
    {
      id: 4,
      title: 'Website Redesign',
      description: 'Update client website with new branding elements',
      priority: 'Medium',
      assignee: 'RB',
      dueDate: '2024-02-25',
    },
  ],
  completed: [
    {
      id: 5,
      title: 'Social Media Audit',
      description: 'Complete social media audit for Global Solutions',
      priority: 'Low',
      assignee: 'JS',
      dueDate: '2024-02-05',
    },
  ],
};

const Tasks = () => {
  return (
    <Box>
      <Box sx={{ display: 'flex', justifyContent: 'space-between', mb: 4 }}>
        <Typography variant="h4">Tasks</Typography>
        <Button
          variant="contained"
          startIcon={<AddIcon />}
          sx={{
            borderRadius: 2,
            px: 3,
          }}
        >
          Add Task
        </Button>
      </Box>

      <Box
        sx={{
          display: 'flex',
          overflowX: 'auto',
          pb: 2,
          gap: 2,
        }}
      >
        {Object.entries(tasks).map(([status, items]) => (
          <KanbanColumn key={status}>
            <Box sx={{ display: 'flex', justifyContent: 'space-between', mb: 3 }}>
              <Typography variant="h6" sx={{ textTransform: 'capitalize' }}>
                {status.replace(/([A-Z])/g, ' $1').trim()}
              </Typography>
              <Chip
                label={items.length}
                size="small"
                sx={{ backgroundColor: 'background.default' }}
              />
            </Box>

            <Reorder.Group
              axis="y"
              values={items}
              onReorder={() => {}}
              layoutScroll
              style={{ padding: '8px 0' }}
            >
              {items.map((task) => (
                <Reorder.Item key={task.id} value={task}>
                  <TaskCard
                    whileHover={{ scale: 1.02 }}
                    whileTap={{ scale: 0.98 }}
                  >
                    <Box sx={{ display: 'flex', justifyContent: 'space-between', mb: 1 }}>
                      <Typography variant="subtitle1" sx={{ fontWeight: 600 }}>
                        {task.title}
                      </Typography>
                      <IconButton size="small">
                        <MoreVertIcon />
                      </IconButton>
                    </Box>
                    
                    <Typography
                      variant="body2"
                      color="text.secondary"
                      sx={{ mb: 2 }}
                    >
                      {task.description}
                    </Typography>

                    <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                      <Box sx={{ display: 'flex', gap: 1, alignItems: 'center' }}>
                        <PriorityChip
                          label={task.priority}
                          priority={task.priority}
                          size="small"
                        />
                        <Typography variant="caption" color="text.secondary">
                          {task.dueDate}
                        </Typography>
                      </Box>
                      <Avatar
                        sx={{
                          width: 24,
                          height: 24,
                          fontSize: '0.875rem',
                          bgcolor: 'primary.main',
                        }}
                      >
                        {task.assignee}
                      </Avatar>
                    </Box>
                  </TaskCard>
                </Reorder.Item>
              ))}
            </Reorder.Group>
          </KanbanColumn>
        ))}
      </Box>
    </Box>
  );
};

export default Tasks;
