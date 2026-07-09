import { Grid, Skeleton } from "@mui/material";

export default function LoadingCards(){

    return(

        <Grid container spacing={3}>

            {[1,2,3,4,5,6].map(i=>(

                <Grid

                    key={i}

                    size={{

                        xs:12,

                        md:6,

                        lg:4,

                    }}

                >

                    <Skeleton

                        variant="rounded"

                        height={190}

                    />

                </Grid>

            ))}

        </Grid>

    );

}