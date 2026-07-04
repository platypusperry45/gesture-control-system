import { Stack, Button } from "@mui/material";
import DashboardCard from "./DashboardCard";

export default function ControlPanel(){

    return(

        <DashboardCard title="Controls">

            <Stack spacing={2}>

                <Button
                    variant="contained"
                    fullWidth
                >
                    Start
                </Button>

                <Button
                    variant="outlined"
                    fullWidth
                >
                    Stop
                </Button>

                <Button
                    color="secondary"
                    variant="outlined"
                    fullWidth
                >
                    Retrain Model
                </Button>

            </Stack>

        </DashboardCard>

    );

}