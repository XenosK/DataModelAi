'use client';

import React from 'react';
import { AppBar, Toolbar, Typography, Button, Box, Container } from '@mui/material';
import Link from 'next/link';
import { usePathname } from 'next/navigation';

const navItems = [
  { label: '首页', path: '/' },
  { label: '仓库', path: '/warehouse' },
  { label: '建表', path: '/datamodel' },
  { label: 'ER关系', path: '/relationship' },
  { label: 'Mcp', path: '/mcp' },
  { label: '员工', path: '/employees' },
];

export default function DashboardLayout({ children }: { children: React.ReactNode }) {
  const pathname = usePathname();

  return (
      <Box>
        <AppBar position="static" color="primary">
          <Toolbar>
            <Typography variant="h6" sx={{ flexGrow: 1 }}>
              数据仓库
            </Typography>
            {navItems.map(item => (
                <Button
                    key={item.path}
                    component={Link}
                    href={item.path}
                    color={pathname === item.path ? 'secondary' : 'inherit'}
                    sx={{ mx: 1 }}
                >
                  {item.label}
                </Button>
            ))}
          </Toolbar>
        </AppBar>
        <Container maxWidth="lg" sx={{ mt: 4 }}>
          {children}
        </Container>
      </Box>
  );
}
