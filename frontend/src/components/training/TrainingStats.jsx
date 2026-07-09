import { useEffect, useState } from "react";

import Grid from "@mui/material/Grid";

import ImageIcon from "@mui/icons-material/Image";
import CategoryIcon from "@mui/icons-material/Category";
import AutoGraphIcon from "@mui/icons-material/AutoGraph";
import CheckCircleIcon from "@mui/icons-material/CheckCircle";

import { motion } from "framer-motion";

import MetricTile from "../ui/MetricTile";

const API = "http://127.0.0.1:8000";

export default function TrainingStats() {

    const [stats, setStats] = useState({

        images: 0,

        classes: 0,

        epochs: 0,

        accuracy: "--",

    });

    useEffect(() => {

        let mounted = true;

        async function load() {

            try {

                const res = await fetch(
                    `${API}/dataset/stats`
                );

                const data = await res.json();

                if (mounted)
                    setStats(data);

            }

            catch (err) {

                console.error(err);

            }

        }

        load();

        const timer = setInterval(load, 3000);

        return () => {

            mounted = false;

            clearInterval(timer);

        };

    }, []);

    const cards = [

        {

            icon: <ImageIcon color="primary" />,

            label: "Dataset Images",

            value: stats.images,

        },

        {

            icon: <CategoryIcon color="primary" />,

            label: "Gesture Classes",

            value: stats.classes,

        },

        {

            icon: <AutoGraphIcon color="primary" />,

            label: "Training Epochs",

            value: stats.epochs,

        },

        {

            icon: <CheckCircleIcon color="success" />,

            label: "Best Accuracy",

            value:
                stats.accuracy === "--"
                    ? "--"
                    : `${stats.accuracy}%`,

        },

    ];

    return (

        <Grid
            container
            spacing={3}
        >

            {

                cards.map((card, index) => (

                    <Grid
                        key={card.label}
                        size={{
                            xs: 12,
                            sm: 6,
                            lg: 3,
                        }}
                    >

                        <motion.div

                            initial={{
                                opacity: 0,
                                y: 20,
                            }}

                            animate={{
                                opacity: 1,
                                y: 0,
                            }}

                            transition={{
                                delay: index * 0.08,
                            }}

                        >

                            <MetricTile

                                icon={card.icon}

                                label={card.label}

                                value={card.value}

                            />

                        </motion.div>

                    </Grid>

                ))

            }

        </Grid>

    );

}