import { createTheme } from "@mui/material/styles";

const theme = createTheme({
    palette: {
        mode: "dark",

        primary: {
            main: "#6366F1",
            light: "#818CF8",
            dark: "#4F46E5",
        },

        secondary: {
            main: "#8B5CF6",
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

        info: {
            main: "#38BDF8",
        },

        background: {
            default: "#070B14",
            paper: "rgba(15,23,42,.78)",
        },

        text: {
            primary: "#F8FAFC",
            secondary: "#94A3B8",
        },

        divider: "rgba(255,255,255,.06)",
    },

    shape: {
        borderRadius: 20,
    },

    typography: {

        fontFamily:
            "'Inter','Segoe UI',Roboto,sans-serif",

        h3: {
            fontWeight: 800,
            letterSpacing: "-.04em",
        },

        h4: {
            fontWeight: 700,
            letterSpacing: "-.03em",
        },

        h5: {
            fontWeight: 700,
        },

        h6: {
            fontWeight: 700,
        },

        subtitle1: {
            fontWeight: 600,
        },

        body1: {
            lineHeight: 1.7,
        },

        body2: {
            lineHeight: 1.65,
        },

        button: {
            textTransform: "none",
            fontWeight: 700,
            letterSpacing: ".02em",
        },
    },

    components: {

        MuiCssBaseline: {
            styleOverrides: {
                body: {
                    background:
                        "#070B14",
                },
            },
        },

        MuiPaper: {

            styleOverrides: {

                root: {

                    backgroundImage: "none",

                    background:
                        "rgba(15,23,42,.78)",

                    backdropFilter:
                        "blur(22px)",

                    WebkitBackdropFilter:
                        "blur(22px)",

                    border:
                        "1px solid rgba(255,255,255,.06)",

                },

            },

        },

        MuiCard: {

            styleOverrides: {

                root: {

                    background:
                        "rgba(15,23,42,.78)",

                    backdropFilter:
                        "blur(22px)",

                    WebkitBackdropFilter:
                        "blur(22px)",

                    border:
                        "1px solid rgba(255,255,255,.06)",

                    borderRadius: 24,

                    boxShadow:
                        "0 18px 55px rgba(0,0,0,.35)",

                    transition:
                        "all .28s ease",

                    "&:hover": {

                        transform:
                            "translateY(-4px)",

                        boxShadow:
                            "0 24px 70px rgba(0,0,0,.45)",

                    },

                },

            },

        },

        MuiDrawer: {

            styleOverrides: {

                paper: {

                    background:
                        "rgba(10,15,28,.95)",

                    backdropFilter:
                        "blur(30px)",

                    borderRight:
                        "1px solid rgba(255,255,255,.06)",

                },

            },

        },

        MuiAppBar: {

            styleOverrides: {

                root: {

                    background:
                        "rgba(7,11,20,.88)",

                    backdropFilter:
                        "blur(30px)",

                    WebkitBackdropFilter:
                        "blur(30px)",

                    boxShadow: "none",

                    borderBottom:
                        "1px solid rgba(255,255,255,.06)",

                },

            },

        },

        MuiButton: {

            defaultProps: {
                disableElevation: true,
            },

            styleOverrides: {

                root: {

                    borderRadius: 14,

                    padding:
                        "10px 22px",

                    fontWeight: 700,

                },

                containedPrimary: {

                    background:
                        "linear-gradient(135deg,#6366F1,#4F46E5)",

                    "&:hover": {

                        background:
                            "linear-gradient(135deg,#4F46E5,#4338CA)",

                    },

                },

            },

        },

        MuiChip: {

            styleOverrides: {

                root: {

                    borderRadius: 999,

                    fontWeight: 600,

                },

            },

        },

        MuiTextField: {

            defaultProps: {

                variant: "outlined",

                size: "medium",

            },

        },

        MuiOutlinedInput: {

            styleOverrides: {

                root: {

                    borderRadius: 14,

                    background:
                        "rgba(255,255,255,.02)",

                },

            },

        },

        MuiToolbar: {

            styleOverrides: {

                root: {

                    minHeight: 72,

                },

            },

        },

    },

});

export default theme;