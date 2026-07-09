import Grid from "@mui/material/Grid";
import { motion, AnimatePresence } from "framer-motion";

import ActionCard from "./ActionCard";

export default function ActionGrid({
    actions,
    onEdit,
    onDelete,
    onTest,
}) {

    const entries = Object.entries(actions);

    return (
        <Grid
            container
            spacing={3}
            sx={{
                width: "100%",
                alignItems: "stretch",
            }}
        >
            <AnimatePresence>
                {entries.map(([gesture, mapping], index) => (
                    <Grid
                        key={gesture}
                        size={{
                            xs: 12,
                            sm: 6,
                            lg: 4,
                        }}
                    >
                        <motion.div
                            layout
                            initial={{
                                opacity: 0,
                                y: 30,
                            }}
                            animate={{
                                opacity: 1,
                                y: 0,
                            }}
                            exit={{
                                opacity: 0,
                                y: -20,
                            }}
                            transition={{
                                duration: 0.35,
                                delay: index * 0.05,
                            }}
                            whileHover={{
                                y: -5,
                            }}
                            style={{
                                height: "100%",
                            }}
                        >
                            <ActionCard
                                gesture={gesture}
                                mapping={mapping}
                                onEdit={onEdit}
                                onDelete={onDelete}
                                onTest={onTest}
                            />
                        </motion.div>
                    </Grid>
                ))}
            </AnimatePresence>
        </Grid>
    );
}