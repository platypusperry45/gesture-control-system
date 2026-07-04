import { Box } from "@mui/material";
import { motion } from "framer-motion";

export default function PageContainer({ children }) {
    return (
        <motion.div
            initial={{ opacity: 0, y: 16 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{
                duration: 0.35,
                ease: "easeOut",
            }}
        >
            <Box
                sx={{
                    width: "100%",
                    maxWidth: 1800,
                    mx: "auto",
                    px: {
                        xs: 2,
                        md: 3,
                        lg: 4,
                    },
                    py: 2,
                }}
            >
                {children}
            </Box>
        </motion.div>
    );
}