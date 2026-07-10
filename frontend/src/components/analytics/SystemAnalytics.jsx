import {
    Stack,
    Typography,
    Chip,
    Grid,
} from "@mui/material";


import MemoryRoundedIcon from "@mui/icons-material/MemoryRounded";
import CameraAltRoundedIcon from "@mui/icons-material/CameraAltRounded";
import ModelTrainingRoundedIcon from "@mui/icons-material/ModelTrainingRounded";
import AccessTimeRoundedIcon from "@mui/icons-material/AccessTimeRounded";
import BackHandRoundedIcon from "@mui/icons-material/BackHandRounded";


import GlassCard from "../ui/GlassCard";



export default function SystemAnalytics({ data }) {


    const runtime = data?.runtime || {};
    const system = data?.system || {};
    const model = data?.model || {};



    const cards = [

        {
            title:"CPU Usage",
            value:`${system.cpu ?? 0}%`,
            icon:<MemoryRoundedIcon color="primary"/>,
        },


        {
            title:"RAM Usage",
            value:`${system.ram ?? 0}%`,
            icon:<MemoryRoundedIcon color="secondary"/>,
        },


        {
            title:"Uptime",
            value:runtime.uptime || "00:00:00",
            icon:<AccessTimeRoundedIcon color="success"/>,
        },


        {
            title:"Camera",
            value:runtime.camera ? "Active":"Offline",
            icon:<CameraAltRoundedIcon color="warning"/>,
        },


        {
            title:"Model",
            value:model.loaded ? "Loaded":"Not Loaded",
            icon:<ModelTrainingRoundedIcon color="info"/>,
        },


        {
            title:"Hand Detection",
            value:runtime.hand_detected
                ? "Detected"
                :"Searching",
            icon:<BackHandRoundedIcon color="error"/>,
        },


    ];



    return (

        <GlassCard

            sx={{

                p:3,

            }}

        >


            <Stack

                spacing={1}

                mb={3}

            >

                <Typography

                    variant="h6"

                    fontWeight={700}

                >

                    System Analytics

                </Typography>


                <Typography

                    variant="body2"

                    color="text.secondary"

                >

                    Live hardware and inference status

                </Typography>


            </Stack>



            <Grid

                container

                spacing={2}

            >


                {
                    cards.map(
                        (card,index)=>(


                        <Grid

                            item

                            xs={12}

                            sm={6}

                            md={4}

                            key={index}

                        >


                            <Stack

                                direction="row"

                                alignItems="center"

                                spacing={2}

                                sx={{

                                    p:2,

                                    borderRadius:2,

                                    background:
                                    "rgba(255,255,255,0.04)",

                                }}

                            >


                                {card.icon}


                                <Stack>


                                    <Typography

                                        variant="body2"

                                        color="text.secondary"

                                    >

                                        {card.title}

                                    </Typography>



                                    <Typography

                                        fontWeight={700}

                                    >

                                        {card.value}

                                    </Typography>


                                </Stack>



                            </Stack>


                        </Grid>


                    ))

                }



            </Grid>


        </GlassCard>


    );

}