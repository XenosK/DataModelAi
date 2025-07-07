import * as React from 'react';
import { NextAppProvider } from '@toolpad/core/nextjs';
import { AppRouterCacheProvider } from '@mui/material-nextjs/v15-appRouter';
import DashboardIcon from '@mui/icons-material/Dashboard';
import PersonIcon from '@mui/icons-material/Person';
import LinearProgress from '@mui/material/LinearProgress'
import type { Navigation } from '@toolpad/core/AppProvider';

import theme from '../theme';
import { usePathname } from 'next/navigation';

export const metadata = {
  title: 'My Toolpad Core Next.js App',
  description: 'This is a sample app built with Toolpad Core and Next.js',
};

const NAVIGATION: Navigation = [
  {
    kind: 'header',
    title: '数据模型',
  },
  {
    kind: 'divider'
  },
  {
    segment: 'warehouse',
    title: '仓库',
    icon: <DashboardIcon />,
  },
  {
    segment: 'datamodel',
    title: '建表',
    icon: <DashboardIcon />,
  },
  {
    segment: 'relationship',
    title: 'ER关系',
    icon: <DashboardIcon />,
  },
  {
    kind: 'header',
    title: '系统管理',
  },
  {
    kind: 'divider'
  },
  {
    segment: 'mcp',
    title: 'Mcp',
    icon: <PersonIcon />,
    // pattern: 'employees{/:employeeId}*',
  },
  {
    segment: 'employees',
    title: 'Employees',
    icon: <PersonIcon />,
    pattern: 'employees{/:employeeId}*',
  },
];

const BRANDING = {
  title: '数据模型AI平台',
};



export default function RootLayout(props: { children: React.ReactNode }) {


  return (
    <html lang="en" data-toolpad-color-scheme="light" suppressHydrationWarning>
      <body>

          <AppRouterCacheProvider options={{ enableCssLayer: true }}>
          <React.Suspense fallback={<LinearProgress />}>
            <NextAppProvider
              navigation={NAVIGATION}
              branding={BRANDING}

              theme={theme}
            >
              {props.children}
            </NextAppProvider>
            </React.Suspense>
          </AppRouterCacheProvider>

      </body>
    </html>
  );
}
