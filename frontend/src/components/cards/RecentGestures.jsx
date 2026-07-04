import {

    List,

    ListItem,

    ListItemText,

} from "@mui/material";

import DashboardCard from "./DashboardCard";

export default function RecentGestures({history}){

    return(

        <DashboardCard title="Recent Gestures">

            <List>

                {history.length===0?

                    <ListItem>

                        <ListItemText primary="No gestures"/>

                    </ListItem>

                :

                history.map((g,index)=>(

                    <ListItem key={index}>

                        <ListItemText primary={g}/>

                    </ListItem>

                ))

                }

            </List>

        </DashboardCard>

    );

}