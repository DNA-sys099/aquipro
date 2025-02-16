import React from 'react';
import { styled } from '@mui/material/styles';
import {
  Box,
  Paper,
  Typography,
  Grid,
  Switch,
  TextField,
  Button,
  Divider,
  Avatar,
  List,
  ListItem,
  ListItemText,
  ListItemSecondaryAction,
} from '@mui/material';
import { motion } from 'framer-motion';

const StyledPaper = styled(Paper)(({ theme }) => ({
  padding: theme.spacing(3),
  borderRadius: theme.shape.borderRadius * 2,
  background: `linear-gradient(45deg, ${theme.palette.background.paper} 0%, ${theme.palette.background.paper} 100%)`,
  boxShadow: '0 8px 32px 0 rgba(31, 38, 135, 0.37)',
  backdropFilter: 'blur(4px)',
  border: '1px solid rgba(255, 255, 255, 0.18)',
}));

const SettingItem = styled(ListItem)(({ theme }) => ({
  padding: theme.spacing(2, 0),
  '&:not(:last-child)': {
    borderBottom: '1px solid rgba(255, 255, 255, 0.12)',
  },
}));

const Settings = () => {
  return (
    <Box>
      <Typography variant="h4" gutterBottom sx={{ mb: 4 }}>
        Settings
      </Typography>

      <Grid container spacing={3}>
        <Grid item xs={12} md={4}>
          <StyledPaper
            component={motion.div}
            initial={{ opacity: 0, x: -20 }}
            animate={{ opacity: 1, x: 0 }}
          >
            <Box sx={{ textAlign: 'center', mb: 3 }}>
              <Avatar
                sx={{
                  width: 100,
                  height: 100,
                  margin: '0 auto',
                  mb: 2,
                  bgcolor: 'primary.main',
                }}
              >
                AG
              </Avatar>
              <Typography variant="h6">Agency Growth</Typography>
              <Typography variant="body2" color="text.secondary">
                admin@agencygrowth.com
              </Typography>
            </Box>
            <Button
              variant="outlined"
              fullWidth
              sx={{ mb: 2 }}
            >
              Change Avatar
            </Button>
            <Button
              variant="contained"
              fullWidth
            >
              Edit Profile
            </Button>
          </StyledPaper>
        </Grid>

        <Grid item xs={12} md={8}>
          <StyledPaper
            component={motion.div}
            initial={{ opacity: 0, x: 20 }}
            animate={{ opacity: 1, x: 0 }}
          >
            <Typography variant="h6" gutterBottom>
              General Settings
            </Typography>
            <List>
              <SettingItem>
                <ListItemText
                  primary="Email Notifications"
                  secondary="Receive email notifications for important updates"
                />
                <ListItemSecondaryAction>
                  <Switch defaultChecked />
                </ListItemSecondaryAction>
              </SettingItem>
              <SettingItem>
                <ListItemText
                  primary="Desktop Notifications"
                  secondary="Show desktop notifications for new tasks"
                />
                <ListItemSecondaryAction>
                  <Switch defaultChecked />
                </ListItemSecondaryAction>
              </SettingItem>
              <SettingItem>
                <ListItemText
                  primary="Weekly Reports"
                  secondary="Receive weekly performance reports"
                />
                <ListItemSecondaryAction>
                  <Switch defaultChecked />
                </ListItemSecondaryAction>
              </SettingItem>
            </List>

            <Divider sx={{ my: 3 }} />

            <Typography variant="h6" gutterBottom>
              Agency Information
            </Typography>
            <Grid container spacing={2}>
              <Grid item xs={12}>
                <TextField
                  fullWidth
                  label="Agency Name"
                  defaultValue="Agency Growth"
                  variant="outlined"
                  sx={{ mb: 2 }}
                />
              </Grid>
              <Grid item xs={12} sm={6}>
                <TextField
                  fullWidth
                  label="Contact Email"
                  defaultValue="admin@agencygrowth.com"
                  variant="outlined"
                  sx={{ mb: 2 }}
                />
              </Grid>
              <Grid item xs={12} sm={6}>
                <TextField
                  fullWidth
                  label="Phone Number"
                  defaultValue="+1 (555) 123-4567"
                  variant="outlined"
                  sx={{ mb: 2 }}
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  fullWidth
                  label="Address"
                  defaultValue="123 Business Street, Suite 100"
                  variant="outlined"
                  multiline
                  rows={2}
                  sx={{ mb: 2 }}
                />
              </Grid>
            </Grid>

            <Divider sx={{ my: 3 }} />

            <Typography variant="h6" gutterBottom>
              Integrations
            </Typography>
            <List>
              <SettingItem>
                <ListItemText
                  primary="Google Calendar"
                  secondary="Sync events and meetings"
                />
                <ListItemSecondaryAction>
                  <Button variant="outlined" size="small">
                    Connect
                  </Button>
                </ListItemSecondaryAction>
              </SettingItem>
              <SettingItem>
                <ListItemText
                  primary="Slack"
                  secondary="Receive notifications in Slack"
                />
                <ListItemSecondaryAction>
                  <Button variant="outlined" size="small" color="success">
                    Connected
                  </Button>
                </ListItemSecondaryAction>
              </SettingItem>
              <SettingItem>
                <ListItemText
                  primary="Zoom"
                  secondary="Automatically create meeting links"
                />
                <ListItemSecondaryAction>
                  <Button variant="outlined" size="small">
                    Connect
                  </Button>
                </ListItemSecondaryAction>
              </SettingItem>
            </List>

            <Box sx={{ mt: 3, display: 'flex', justifyContent: 'flex-end', gap: 2 }}>
              <Button variant="outlined">
                Cancel
              </Button>
              <Button variant="contained">
                Save Changes
              </Button>
            </Box>
          </StyledPaper>
        </Grid>
      </Grid>
    </Box>
  );
};

export default Settings;
