import {

    Chip,

    Stack,

} from "@mui/material";

import DashboardCard from "./DashboardCard";

export default function StatusCard({status}){

    return(

        <DashboardCard title="System Status">

            <Stack spacing={2}>

                <Chip

                    color={status.camera?"success":"error"}

                    label={status.camera?"Camera Online":"Camera Offline"}

                />

                <Chip

                    color={status.model_loaded?"success":"error"}

                    label={status.model_loaded?"Model Loaded":"Model Missing"}

                />

                <Chip

                    color={status.inference_running?"success":"warning"}

                    label={status.inference_running?"Inference Running":"Stopped"}

                />

            </Stack>

        </DashboardCard>

    );

}