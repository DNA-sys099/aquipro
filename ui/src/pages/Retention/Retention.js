import React, { useState } from 'react';
import {
  Box,
  Grid,
  Paper,
  Typography,
  Card,
  CardContent,
  LinearProgress,
  Button,
  Tab,
  Tabs,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
} from '@mui/material';
import {
  Timeline,
  TimelineItem,
  TimelineSeparator,
  TimelineConnector,
  TimelineContent,
  TimelineDot,
} from '@mui/lab';
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
} from 'recharts';

const retentionData = [
  { month: 'Jan', retention: 95 },
  { month: 'Feb', retention: 92 },
  { month: 'Mar', retention: 96 },
  { month: 'Apr', retention: 94 },
  { month: 'May', retention: 97 },
  { month: 'Jun', retention: 95 },
];

const clientHealthData = [
  {
    client: 'Tech Solutions Inc',
    health: 95,
    status: 'Healthy',
    lastContact: '2 days ago',
    nextReview: '15 days',
  },
  {
    client: 'Marketing Pro',
    health: 82,
    status: 'At Risk',
    lastContact: '5 days ago',
    nextReview: '7 days',
  },
  {
    client: 'Global Services',
    health: 88,
    status: 'Stable',
    lastContact: '1 day ago',
    nextReview: '30 days',
  },
];

const RetentionPage = () => {
  const [tabValue, setTabValue] = useState(0);

  const handleTabChange = (event, newValue) => {
    setTabValue(newValue);
  };

  return (
    <Box sx={{ p: 3 }}>
      <Typography variant="h4" gutterBottom>
        Client Retention Dashboard
      </Typography>

      <Grid container spacing={3}>
        {/* Overview Cards */}
        <Grid item xs={12} md={4}>
          <Card>
            <CardContent>
              <Typography variant="h6">Overall Retention Rate</Typography>
              <Typography variant="h3" color="primary">
                94.8%
              </Typography>
              <LinearProgress
                variant="determinate"
                value={94.8}
                sx={{ mt: 2 }}
              />
            </CardContent>
          </Card>
        </Grid>

        <Grid item xs={12} md={4}>
          <Card>
            <CardContent>
              <Typography variant="h6">Average Client Health</Typography>
              <Typography variant="h3" color="primary">
                88.3%
              </Typography>
              <LinearProgress
                variant="determinate"
                value={88.3}
                sx={{ mt: 2 }}
              />
            </CardContent>
          </Card>
        </Grid>

        <Grid item xs={12} md={4}>
          <Card>
            <CardContent>
              <Typography variant="h6">Client Satisfaction</Typography>
              <Typography variant="h3" color="primary">
                4.7/5
              </Typography>
              <LinearProgress
                variant="determinate"
                value={(4.7 / 5) * 100}
                sx={{ mt: 2 }}
              />
            </CardContent>
          </Card>
        </Grid>

        {/* Retention Chart */}
        <Grid item xs={12} md={8}>
          <Paper sx={{ p: 2 }}>
            <Typography variant="h6" gutterBottom>
              Retention Trend
            </Typography>
            <Box sx={{ height: 300 }}>
              <ResponsiveContainer width="100%" height="100%">
                <BarChart data={retentionData}>
                  <CartesianGrid strokeDasharray="3 3" />
                  <XAxis dataKey="month" />
                  <YAxis domain={[80, 100]} />
                  <Tooltip />
                  <Bar dataKey="retention" fill="#2196f3" />
                </BarChart>
              </ResponsiveContainer>
            </Box>
          </Paper>
        </Grid>

        {/* Timeline */}
        <Grid item xs={12} md={4}>
          <Paper sx={{ p: 2 }}>
            <Typography variant="h6" gutterBottom>
              Recent Activities
            </Typography>
            <Timeline>
              <TimelineItem>
                <TimelineSeparator>
                  <TimelineDot color="primary" />
                  <TimelineConnector />
                </TimelineSeparator>
                <TimelineContent>
                  <Typography variant="subtitle2">
                    Quarterly Review - Tech Solutions
                  </Typography>
                  <Typography variant="body2" color="textSecondary">
                    2 hours ago
                  </Typography>
                </TimelineContent>
              </TimelineItem>
              <TimelineItem>
                <TimelineSeparator>
                  <TimelineDot color="primary" />
                  <TimelineConnector />
                </TimelineSeparator>
                <TimelineContent>
                  <Typography variant="subtitle2">
                    Health Score Update
                  </Typography>
                  <Typography variant="body2" color="textSecondary">
                    1 day ago
                  </Typography>
                </TimelineContent>
              </TimelineItem>
              <TimelineItem>
                <TimelineSeparator>
                  <TimelineDot color="primary" />
                </TimelineSeparator>
                <TimelineContent>
                  <Typography variant="subtitle2">
                    Client Feedback Received
                  </Typography>
                  <Typography variant="body2" color="textSecondary">
                    2 days ago
                  </Typography>
                </TimelineContent>
              </TimelineItem>
            </Timeline>
          </Paper>
        </Grid>

        {/* Client Health Table */}
        <Grid item xs={12}>
          <Paper sx={{ p: 2 }}>
            <Box sx={{ borderBottom: 1, borderColor: 'divider', mb: 2 }}>
              <Tabs value={tabValue} onChange={handleTabChange}>
                <Tab label="Client Health" />
                <Tab label="Action Items" />
                <Tab label="Reviews" />
              </Tabs>
            </Box>

            {tabValue === 0 && (
              <TableContainer>
                <Table>
                  <TableHead>
                    <TableRow>
                      <TableCell>Client</TableCell>
                      <TableCell>Health Score</TableCell>
                      <TableCell>Status</TableCell>
                      <TableCell>Last Contact</TableCell>
                      <TableCell>Next Review</TableCell>
                      <TableCell>Action</TableCell>
                    </TableRow>
                  </TableHead>
                  <TableBody>
                    {clientHealthData.map((row) => (
                      <TableRow key={row.client}>
                        <TableCell>{row.client}</TableCell>
                        <TableCell>
                          <Box sx={{ display: 'flex', alignItems: 'center' }}>
                            {row.health}%
                            <LinearProgress
                              variant="determinate"
                              value={row.health}
                              sx={{ ml: 1, width: 100 }}
                            />
                          </Box>
                        </TableCell>
                        <TableCell>{row.status}</TableCell>
                        <TableCell>{row.lastContact}</TableCell>
                        <TableCell>{row.nextReview}</TableCell>
                        <TableCell>
                          <Button variant="contained" size="small">
                            View Details
                          </Button>
                        </TableCell>
                      </TableRow>
                    ))}
                  </TableBody>
                </Table>
              </TableContainer>
            )}
          </Paper>
        </Grid>
      </Grid>
    </Box>
  );
};

export default RetentionPage;
