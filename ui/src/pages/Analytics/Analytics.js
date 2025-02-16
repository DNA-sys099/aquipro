import React from 'react';
import { styled } from '@mui/material/styles';
import {
  Box,
  Paper,
  Typography,
  Grid,
  MenuItem,
  Select,
  FormControl,
} from '@mui/material';
import { Line, Bar, Doughnut } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  BarElement,
  ArcElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  BarElement,
  ArcElement,
  Title,
  Tooltip,
  Legend
);

const StyledPaper = styled(Paper)(({ theme }) => ({
  padding: theme.spacing(3),
  borderRadius: theme.shape.borderRadius * 2,
  background: `linear-gradient(45deg, ${theme.palette.background.paper} 0%, ${theme.palette.background.paper} 100%)`,
  boxShadow: '0 8px 32px 0 rgba(31, 38, 135, 0.37)',
  backdropFilter: 'blur(4px)',
  border: '1px solid rgba(255, 255, 255, 0.18)',
}));

const MetricCard = styled(StyledPaper)(({ theme }) => ({
  padding: theme.spacing(3),
  display: 'flex',
  flexDirection: 'column',
  height: '100%',
}));

const chartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    legend: {
      position: 'bottom',
      labels: {
        color: 'rgba(255, 255, 255, 0.7)',
      },
    },
  },
  scales: {
    x: {
      grid: {
        display: false,
      },
      ticks: {
        color: 'rgba(255, 255, 255, 0.7)',
      },
    },
    y: {
      grid: {
        color: 'rgba(255, 255, 255, 0.1)',
      },
      ticks: {
        color: 'rgba(255, 255, 255, 0.7)',
      },
    },
  },
};

const revenueData = {
  labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
  datasets: [
    {
      label: 'Revenue',
      data: [30000, 45000, 57000, 48000, 65000, 75000],
      borderColor: '#2196f3',
      backgroundColor: 'rgba(33, 150, 243, 0.1)',
      fill: true,
      tension: 0.4,
    },
  ],
};

const clientGrowthData = {
  labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
  datasets: [
    {
      label: 'New Clients',
      data: [5, 7, 4, 8, 6, 9],
      backgroundColor: '#4caf50',
    },
    {
      label: 'Churned Clients',
      data: [2, 1, 2, 1, 1, 2],
      backgroundColor: '#f44336',
    },
  ],
};

const serviceDistributionData = {
  labels: ['SEO', 'PPC', 'Social Media', 'Content', 'Web Dev'],
  datasets: [
    {
      data: [35, 25, 20, 15, 5],
      backgroundColor: [
        '#2196f3',
        '#4caf50',
        '#ff9800',
        '#f44336',
        '#9c27b0',
      ],
    },
  ],
};

const Analytics = () => {
  const [timeRange, setTimeRange] = React.useState('6m');

  return (
    <Box>
      <Box sx={{ display: 'flex', justifyContent: 'space-between', mb: 4 }}>
        <Typography variant="h4">Analytics</Typography>
        <FormControl sx={{ minWidth: 120 }}>
          <Select
            value={timeRange}
            onChange={(e) => setTimeRange(e.target.value)}
            size="small"
            sx={{ borderRadius: 2 }}
          >
            <MenuItem value="1m">Last Month</MenuItem>
            <MenuItem value="3m">Last 3 Months</MenuItem>
            <MenuItem value="6m">Last 6 Months</MenuItem>
            <MenuItem value="1y">Last Year</MenuItem>
          </Select>
        </FormControl>
      </Box>

      <Grid container spacing={3}>
        <Grid item xs={12} md={3}>
          <MetricCard>
            <Typography variant="h6" gutterBottom>
              Total Revenue
            </Typography>
            <Typography variant="h4" sx={{ mb: 1 }}>
              $320,500
            </Typography>
            <Typography variant="body2" color="success.main">
              +15.3% vs last period
            </Typography>
          </MetricCard>
        </Grid>
        <Grid item xs={12} md={3}>
          <MetricCard>
            <Typography variant="h6" gutterBottom>
              Active Clients
            </Typography>
            <Typography variant="h4" sx={{ mb: 1 }}>
              39
            </Typography>
            <Typography variant="body2" color="success.main">
              +4 vs last period
            </Typography>
          </MetricCard>
        </Grid>
        <Grid item xs={12} md={3}>
          <MetricCard>
            <Typography variant="h6" gutterBottom>
              Average Revenue
            </Typography>
            <Typography variant="h4" sx={{ mb: 1 }}>
              $8,218
            </Typography>
            <Typography variant="body2" color="success.main">
              +5.2% vs last period
            </Typography>
          </MetricCard>
        </Grid>
        <Grid item xs={12} md={3}>
          <MetricCard>
            <Typography variant="h6" gutterBottom>
              Client Retention
            </Typography>
            <Typography variant="h4" sx={{ mb: 1 }}>
              94.5%
            </Typography>
            <Typography variant="body2" color="success.main">
              +2.1% vs last period
            </Typography>
          </MetricCard>
        </Grid>

        <Grid item xs={12} md={8}>
          <StyledPaper>
            <Typography variant="h6" gutterBottom>
              Revenue Growth
            </Typography>
            <Box sx={{ height: 400 }}>
              <Line options={chartOptions} data={revenueData} />
            </Box>
          </StyledPaper>
        </Grid>

        <Grid item xs={12} md={4}>
          <StyledPaper>
            <Typography variant="h6" gutterBottom>
              Service Distribution
            </Typography>
            <Box sx={{ height: 400 }}>
              <Doughnut
                data={serviceDistributionData}
                options={{
                  ...chartOptions,
                  cutout: '70%',
                }}
              />
            </Box>
          </StyledPaper>
        </Grid>

        <Grid item xs={12}>
          <StyledPaper>
            <Typography variant="h6" gutterBottom>
              Client Growth
            </Typography>
            <Box sx={{ height: 400 }}>
              <Bar options={chartOptions} data={clientGrowthData} />
            </Box>
          </StyledPaper>
        </Grid>
      </Grid>
    </Box>
  );
};

export default Analytics;
