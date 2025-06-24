import React from 'react';
import { Container, Typography, Box } from '@mui/material';

const JobListingsPage: React.FC = () => {
  return (
    <Container maxWidth="lg" sx={{ mt: 4 }}>
      <Box textAlign="center">
        <Typography variant="h4" gutterBottom>
          Job Listings - Coming Soon
        </Typography>
        <Typography variant="body1">
          Job listings functionality will be implemented here.
        </Typography>
      </Box>
    </Container>
  );
};

export default JobListingsPage;
