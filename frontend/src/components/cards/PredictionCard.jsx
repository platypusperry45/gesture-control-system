
import {

    Typography,

    LinearProgress,

} from "@mui/material";

import DashboardCard from "./DashboardCard";

export default function PredictionCard({status}){

    return(

        <DashboardCard title="Current Gesture">

            <Typography

                variant="h3"

                fontWeight={700}

            >

                {status.prediction ?? "--"}

            </Typography>

            <Typography mt={2}>

                Confidence {(status.confidence*100).toFixed(1)}%

            </Typography>

            <LinearProgress

                sx={{mt:1}}

                variant="determinate"

                value={status.confidence*100}

            />

            <Typography mt={3}>

                Action

            </Typography>

            <Typography fontWeight={600}>

                {status.action ?? "--"}

            </Typography>

        </DashboardCard>

    );

}