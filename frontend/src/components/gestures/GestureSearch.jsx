import {
    TextField,
} from "@mui/material";

export default function GestureSearch({
    value,
    onChange,
}) {

    return (

        <TextField

            fullWidth

            placeholder="Search gestures..."

            value={value}

            onChange={(e)=>

                onChange(e.target.value)

            }

            sx={{
                mb:4,
            }}

        />

    );

}