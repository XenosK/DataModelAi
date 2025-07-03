'use client';
import * as React from 'react';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';
import CardActionArea from '@mui/material/CardActionArea';
import { PageContainer } from '@toolpad/core/PageContainer';
import AppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import Button from '@mui/material/Button';
import IconButton from '@mui/material/IconButton';
import MenuIcon from '@mui/icons-material/Menu';

const cards = [
    {
        id: 1,
        title: 'DWD层',
        description: '数据明细层的表',
    },
    {
        id: 2,
        title: 'sap系统',
        description: 'SAP系统的表',
    },
    {
        id: 3,
        title: 'DS数据',
        description: 'DataService上报数据的表',
    },
    {
        id: 3,
        title: 'DS数据',
        description: 'DataService上报数据的表',
    },
    {
        id: 3,
        title: 'DS数据',
        description: 'DataService上报数据的表',
    },
    {
        id: 3,
        title: 'DS数据',
        description: 'DataService上报数据的表',
    },
];

function SelectActionCard() {
    const [selectedCard, setSelectedCard] = React.useState(0);
    return (
        <PageContainer>
            <Typography variant="h6"
                        gutterBottom
                        sx={{
                            width: '100%',
                            display: 'grid',
                            gridTemplateColumns: 'repeat(auto-fill, minmax(min(200px, 100%), 1fr))',
                            gap: 2,
                            pt:2,
                        }}
            >
                分系统模型
            </Typography>
            <Box
                sx={{
                    width: '100%',
                    display: 'grid',
                    gridTemplateColumns: 'repeat(auto-fill, minmax(min(200px, 100%), 1fr))',
                    gap: 2,
                }}
            >


                {cards.map((card, index) => (
                    // eslint-disable-next-line react/jsx-key
                    <Card>
                        <CardActionArea
                            onClick={() => setSelectedCard(index)}
                            data-active={selectedCard === index ? '' : undefined}
                            sx={{
                                height: '100%',
                                '&[data-active]': {
                                    backgroundColor: 'action.selected',
                                    '&:hover': {
                                        backgroundColor: 'action.selectedHover',
                                    },
                                },
                            }}
                        >
                            <CardContent sx={{ height: '100%' }}>
                                <Typography variant="h5" component="div">
                                    {card.title}
                                </Typography>
                                <Typography variant="body2" color="text.secondary">
                                    {card.description}
                                </Typography>
                            </CardContent>
                        </CardActionArea>
                    </Card>
                ))}
            </Box>
            <Typography variant="h6"
                        gutterBottom
                        sx={{
                            width: '100%',
                            display: 'grid',
                            gridTemplateColumns: 'repeat(auto-fill, minmax(min(200px, 100%), 1fr))',
                            gap: 2,
                            pt:5,
                        }}
            >
                分系统模型
            </Typography>
            <Box
                sx={{
                    width: '100%',
                    display: 'grid',
                    gridTemplateColumns: 'repeat(auto-fill, minmax(min(200px, 100%), 1fr))',
                    gap: 2,
                }}
            >
                {cards.map((card, index) => (
                    // eslint-disable-next-line react/jsx-key
                    <Card>
                        <CardActionArea
                            onClick={() => setSelectedCard(index)}
                            data-active={selectedCard === index ? '' : undefined}
                            sx={{
                                height: '100%',
                                '&[data-active]': {
                                    backgroundColor: 'action.selected',
                                    '&:hover': {
                                        backgroundColor: 'action.selectedHover',
                                    },
                                },
                            }}
                        >
                            <CardContent sx={{ height: '100%' }}>
                                <Typography variant="h5" component="div">
                                    {card.title}
                                </Typography>
                                <Typography variant="body2" color="text.secondary">
                                    {card.description}
                                </Typography>
                            </CardContent>
                        </CardActionArea>
                    </Card>
                ))}
            </Box>
        </PageContainer>
    );
}

export default SelectActionCard;

