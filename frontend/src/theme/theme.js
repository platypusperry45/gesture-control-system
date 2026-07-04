import { createTheme } from "@mui/material/styles";

const theme = createTheme({

    palette: {

        mode: "dark",

        primary: {
            main: "#5B8CFF",
        },

        secondary: {
            main: "#7C4DFF",
        },

        background: {

            default: "#0B1020",

            paper: "#151B2F",

        },

        success: {
            main: "#22C55E",
        },

        warning: {
            main: "#F59E0B",
        },

        error: {
            main: "#EF4444",
        },

        text: {

            primary: "#F8FAFC",

            secondary: "#94A3B8",

        },

    },

    shape: {

        borderRadius: 18,

    },

    typography: {

        fontFamily:

            "'Inter', 'Segoe UI', sans-serif",

        h3: {

            fontWeight: 700,

        },

        h4: {

            fontWeight: 700,

        },

        h5: {

            fontWeight: 600,

        },

        h6: {

            fontWeight: 600,

        },

        button: {

            textTransform: "none",

            fontWeight: 600,

        },

    },

    components: {

        MuiCard: {

            styleOverrides: {

                root: {

                    borderRadius: 20,

                    background:

                        "rgba(21,27,47,0.82)",

                    backdropFilter:

                        "blur(20px)",

                    border:

                        "1px solid rgba(255,255,255,0.05)",

                    boxShadow:

                        "0 15px 40px rgba(0,0,0,.35)",

                },

            },

        },

        MuiButton: {

            styleOverrides: {

                root: {

                    borderRadius: 14,

                    padding: "10px 22px",

                },

            },

        },

    },

});

export default theme;