import Grid from "@mui/material/Grid";

import GestureCard from "./GestureCard";

export default function GestureGrid({
    gestures,
}) {

    return (

        <Grid
            container
            spacing={3}
        >

            {gestures.map((gesture)=>(

                <Grid
                    key={gesture.id}
                    size={{
                        xs:12,
                        sm:6,
                        md:4,
                        lg:3,
                    }}
                >

                    <GestureCard
                        gesture={gesture}
                    />

                </Grid>

            ))}

        </Grid>

    );

}