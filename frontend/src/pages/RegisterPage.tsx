import React from 'react';
import { Container, Typography, Box } from '@mui/material';

const RegisterPage: React.FC = () => {
  return (
    <Container maxWidth="sm" sx={{ mt: 8 }}>
      <Box textAlign="center">
        <Typography variant="h4" gutterBottom>
          Register - Coming Soon
        </Typography>
        <Typography variant="body1">
          Registration functionality will be implemented here.
        </Typography>
      </Box>
    </Container>
  );
};

export default RegisterPage;
