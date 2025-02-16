import React from 'react';
import { styled } from '@mui/material/styles';
import Grid from '@mui/material/Grid';
import Paper from '@mui/material/Paper';
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box';
import { motion } from 'framer-motion';
import { Line } from 'react-chartjs-2';
import TrendingUpIcon from '@mui/icons-material/TrendingUp';
import PeopleIcon from '@mui/icons-material/People';
import AttachMoneyIcon from '@mui/icons-material/AttachMoney';
import TaskIcon from '@mui/icons-material/Task';

const StyledPaper = styled(Paper)(({ theme }) => ({
  padding: theme.spacing(3),
  borderRadius: theme.shape.borderRadius * 2,
  background: `linear-gradient(45deg, ${theme.palette.background.paper} 0%, ${theme.palette.background.paper} 100%)`,
  boxShadow: '0 8px 32px 0 rgba(31, 38, 135, 0.37)',
  backdropFilter: 'blur(4px)',
  border: '1px solid rgba(255, 255, 255, 0.18)',
}));

const MetricCard = styled(motion(StyledPaper))(({ theme }) => ({
  display: 'flex',
  flexDirection: 'column',
  height: '100%',
  minHeight: 140,
}));

const chartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    legend: {
      display: false,
    },
  },
  scales: {
    x: {
      grid: {
        display: false,
      },
    },
    y: {
      grid: {
        color: 'rgba(255, 255, 255, 0.1)',
      },
    },
  },
};

const chartData = {
  labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
  datasets: [
    {
      label: 'Revenue',
      data: [30, 45, 57, 48, 65, 75],
      fill: false,
      borderColor: '#2196f3',
      tension: 0.4,
    },
  ],
};

const metrics = [
  {
    title: 'Total Revenue',
    value: '$75,430',
    change: '+12.5%',
    icon: <AttachMoneyIcon sx={{ fontSize: 40, color: 'primary.main' }} />,
  },
  {
    title: 'Active Clients',
    value: '24',
    change: '+3',
    icon: <PeopleIcon sx={{ fontSize: 40, color: 'secondary.main' }} />,
  },
  {
    title: 'Tasks Completed',
    value: '156',
    change: '+23%',
    icon: <TaskIcon sx={{ fontSize: 40, color: 'success.main' }} />,
  },
  {
    title: 'Growth Rate',
    value: '18.2%',
    change: '+2.4%',
    icon: <TrendingUpIcon sx={{ fontSize: 40, color: 'warning.main' }} />,
  },
];

const Dashboard = () => {
  return (
    <Box>
      <Typography variant="h4" gutterBottom sx={{ mb: 4 }}>
        Dashboard
      </Typography>
      
      <Grid container spacing={3}>
        {metrics.map((metric, index) => (
          <Grid item xs={12} sm={6} md={3} key={index}>
            <MetricCard
              whileHover={{ y: -5 }}
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: index * 0.1 }}
            >
              <Box sx={{ display: 'flex', justifyContent: 'space-between', mb: 2 }}>
                {metric.icon}
                <Typography
                  variant="caption"
                  sx={{
                    color: 'success.main',
                    backgroundColor: 'success.main',
                    px: 1,
                    py: 0.5,
                    borderRadius: 1,
                    opacity: 0.2,
                  }}
                >
                  {metric.change}
                </Typography>
              </Box>
              <Typography variant="h4" sx={{ mb: 1 }}>
                {metric.value}
              </Typography>
              <Typography variant="body2" color="text.secondary">
                {metric.title}
              </Typography>
            </MetricCard>
          </Grid>
        ))}

        <Grid item xs={12} md={8}>
          <StyledPaper sx={{ height: 400, p: 3 }}>
            <Typography variant="h6" gutterBottom>
              Revenue Overview
            </Typography>
            <Box sx={{ height: 300 }}>
              <Line data={chartData} options={chartOptions} />
            </Box>
          </StyledPaper>
        </Grid>

        <Grid item xs={12} md={4}>
          <StyledPaper sx={{ height: 400, p: 3 }}>
            <Typography variant="h6" gutterBottom>
              Recent Activity
            </Typography>
            <Box sx={{ mt: 2 }}>
              {[1, 2, 3, 4].map((item) => (
                <Box
                  key={item}
                  sx={{
                    py: 2,
                    borderBottom: '1px solid rgba(255, 255, 255, 0.12)',
                    '&:last-child': { borderBottom: 'none' },
                  }}
                >
                  <Typography variant="body2" color="text.secondary">
                    {item} hour ago
                  </Typography>
                  <Typography variant="body1">
                    New client onboarding completed
                  </Typography>
                </Box>
              ))}
            </Box>
          </StyledPaper>
        </Grid>
      </Grid>
    </Box>
  );
};

export default Dashboard;
