import {

    Drawer,

    Toolbar,

    List,

    ListItemButton,

    ListItemIcon,

    ListItemText,

} from "@mui/material";

import DashboardIcon from "@mui/icons-material/Dashboard";
import PanToolIcon from "@mui/icons-material/PanTool";
import KeyboardIcon from "@mui/icons-material/Keyboard";
import ModelTrainingIcon from "@mui/icons-material/ModelTraining";
import AnalyticsIcon from "@mui/icons-material/Analytics";
import SettingsIcon from "@mui/icons-material/Settings";

const drawerWidth = 260;

const menu = [

    {
        name:"Dashboard",
        icon:<DashboardIcon/>
    },

    {
        name:"Gestures",
        icon:<PanToolIcon/>
    },

    {
        name:"Actions",
        icon:<KeyboardIcon/>
    },

    {
        name:"Training",
        icon:<ModelTrainingIcon/>
    },

    {
        name:"Analytics",
        icon:<AnalyticsIcon/>
    },

    {
        name:"Settings",
        icon:<SettingsIcon/>
    },

];

export default function SideNavigation(){

    return(

        <Drawer

            variant="permanent"

            sx={{

                width:drawerWidth,

                flexShrink:0,

                "& .MuiDrawer-paper":{

                    width:drawerWidth,

                    bgcolor:"#10182E",

                    borderRight:"1px solid rgba(255,255,255,.05)",

                }

            }}

        >

            <Toolbar/>

            <List sx={{mt:2}}>

                {menu.map(item=>(

                    <ListItemButton

                        key={item.name}

                        sx={{

                            mx:2,

                            my:.5,

                            borderRadius:3,

                        }}

                    >

                        <ListItemIcon>

                            {item.icon}

                        </ListItemIcon>

                        <ListItemText

                            primary={item.name}

                        />

                    </ListItemButton>

                ))}

            </List>

        </Drawer>

    );

}
    

