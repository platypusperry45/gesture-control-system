import {
    Typography,
    Stack,
} from "@mui/material";

import {
    BarChart,
    Bar,
    XAxis,
    YAxis,
    Tooltip,
    ResponsiveContainer,
} from "recharts";


import GlassCard from "../ui/GlassCard";



export default function PredictionAnalytics({data}) {


    const distribution =
        data?.runtime?.prediction_distribution || {};



    const chartData =
        Object.entries(distribution).map(
            ([gesture,count])=>({

                gesture,

                count,

            })
        );



    return (

        <GlassCard

            sx={{

                p:3,

                height:360,

            }}

        >


            <Stack

                spacing={1}

                mb={2}

            >

                <Typography

                    variant="h6"

                    fontWeight={700}

                >

                    Prediction Distribution

                </Typography>


                <Typography

                    variant="body2"

                    color="text.secondary"

                >

                    Live gesture recognition frequency

                </Typography>


            </Stack>



            {

                chartData.length === 0 ?


                (

                    <Typography

                        color="text.secondary"

                    >

                        No predictions yet

                    </Typography>

                )


                :

                (

                    <ResponsiveContainer

                        width="100%"

                        height="85%"

                    >

                        <BarChart

                            data={chartData}

                        >

                            <XAxis

                                dataKey="gesture"

                            />


                            <YAxis/>


                            <Tooltip/>


                            <Bar

                                dataKey="count"

                                radius={[8,8,0,0]}

                            />


                        </BarChart>


                    </ResponsiveContainer>

                )

            }



        </GlassCard>

    );

}