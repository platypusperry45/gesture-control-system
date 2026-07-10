import {useEffect,useState} from "react";

import {
Box,
Stack,
Typography,
Switch,
FormControl,
Select,
MenuItem,
InputLabel,
Divider,
Button,
} from "@mui/material";


import SettingsRoundedIcon from "@mui/icons-material/SettingsRounded";
import DarkModeRoundedIcon from "@mui/icons-material/DarkModeRounded";
import NotificationsRoundedIcon from "@mui/icons-material/NotificationsRounded";
import SaveRoundedIcon from "@mui/icons-material/SaveRounded";

import GlassCard from "../ui/GlassCard";

import api from "../../services/api";


export default function GeneralSettings(){


const [settings,setSettings]=useState(null);



useEffect(()=>{

loadSettings();

},[]);



async function loadSettings(){

const res=await api.get("/settings");

setSettings(res.data);

}



function update(key,value){

setSettings({

...settings,

[key]:value

});

}



async function save(){

await api.post(
"/settings",
settings
);

}



if(!settings)
return null;



return (

<GlassCard
sx={{
p:3,
height:"100%"
}}
>


<Stack
direction="row"
spacing={1}
alignItems="center"
mb={3}
>

<SettingsRoundedIcon color="primary"/>

<Typography
variant="h6"
fontWeight={700}
>
General Settings
</Typography>

</Stack>



<Stack spacing={3}>


<FormControl fullWidth>

<InputLabel>
Theme
</InputLabel>


<Select

value={settings.theme}

label="Theme"

onChange={(e)=>
update(
"theme",
e.target.value
)
}

>


<MenuItem value="Dark">
Dark
</MenuItem>


<MenuItem value="Light">
Light
</MenuItem>


<MenuItem value="System">
System
</MenuItem>


</Select>

</FormControl>



<Divider/>



<Stack
direction="row"
justifyContent="space-between"
alignItems="center"
>


<Stack
direction="row"
spacing={1}
alignItems="center"
>

<DarkModeRoundedIcon color="primary"/>

<Typography>
Enable Dark Theme
</Typography>

</Stack>


<Switch

checked={
settings.theme==="Dark"
}

onChange={(e)=>

update(
"theme",
e.target.checked?
"Dark":
"Light"
)

}

/>

</Stack>





<Stack
direction="row"
justifyContent="space-between"
alignItems="center"
>


<Stack
direction="row"
spacing={1}
alignItems="center"
>

<NotificationsRoundedIcon color="primary"/>

<Typography>
Notifications
</Typography>

</Stack>


<Switch

checked={
settings.notifications
}

onChange={(e)=>

update(
"notifications",
e.target.checked
)

}

/>

</Stack>





<Stack
direction="row"
justifyContent="space-between"
alignItems="center"
>


<Stack
direction="row"
spacing={1}
alignItems="center"
>

<SaveRoundedIcon color="primary"/>

<Typography>
Auto Save Settings
</Typography>

</Stack>


<Switch

checked={
settings.autoSave
}

onChange={(e)=>

update(
"autoSave",
e.target.checked
)

}

/>

</Stack>



<Divider/>


<Button

fullWidth

variant="contained"

size="large"

onClick={save}

>

Save Preferences

</Button>


</Stack>


</GlassCard>

);

}