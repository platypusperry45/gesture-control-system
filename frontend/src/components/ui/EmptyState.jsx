import { Box, Typography } from "@mui/material";
import PanToolAltIcon from "@mui/icons-material/PanToolAlt";

export default function EmptyState({

    title,

    subtitle,

}){

    return(

        <Box

            sx={{

                py:10,

                textAlign:"center",

                opacity:.8,

            }}

        >

            <PanToolAltIcon

                sx={{

                    fontSize:70,

                    color:"primary.main",

                    mb:2,

                }}

            />

            <Typography

                variant="h5"

                fontWeight={700}

            >

                {title}

            </Typography>

            <Typography

                color="text.secondary"

            >

                {subtitle}

            </Typography>

        </Box>

    );

}