import {

    Typography,

    Stack,

} from "@mui/material";

import DashboardCard from "./DashboardCard";

export default function MetricsCard({status}){

    return(

        <DashboardCard title="Performance">

            <Stack spacing={2}>

                <Typography variant="h4">

                    {status.fps}

                </Typography>

                <Typography>

                    FPS

                </Typography>

                <Typography>

                    Uptime

                </Typography>

                <Typography fontWeight={700}>

                    {status.uptime}

                </Typography>

            </Stack>

        </DashboardCard>

    );

}