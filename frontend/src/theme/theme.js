import { createTheme } from "@mui/material/styles";

const theme = createTheme({
    palette: {
        mode: "dark",

        primary: {
            main: "#6366F1",
        },

        secondary: {
            main: "#8B5CF6",
        },

        background: {
            default: "#090C15",
            paper: "#121826",
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

        divider: "rgba(255,255,255,.08)",

        text: {
            primary: "#F8FAFC",
            secondary: "#94A3B8",
        },
    },

    shape: {
        borderRadius: 20,
    },

    typography: {
        fontFamily: "'Inter','Segoe UI',sans-serif",

        h3: {
            fontWeight: 700,
            letterSpacing: "-0.03em",
        },

        h4: {
            fontWeight: 700,
            letterSpacing: "-0.02em",
        },

        h5: {
            fontWeight: 600,
            letterSpacing: "-0.02em",
        },

        h6: {
            fontWeight: 600,
        },

        subtitle1: {
            fontWeight: 500,
        },

        body1: {
            lineHeight: 1.7,
        },

        body2: {
            lineHeight: 1.6,
        },

        button: {
            textTransform: "none",
            fontWeight: 600,
            letterSpacing: ".02em",
        },
    },

    components: {

        MuiCssBaseline: {
            styleOverrides: {
                body: {
                    background: `
                        radial-gradient(circle at top,
                        rgba(99,102,241,.12),
                        transparent 35%),
                        #090C15
                    `,
                },
            },
        },

        MuiCard: {
            styleOverrides: {
                root: {
                    background: "rgba(18,24,38,.72)",

                    backdropFilter: "blur(20px)",
                    WebkitBackdropFilter: "blur(20px)",

                    border: "1px solid rgba(255,255,255,.06)",

                    borderRadius: 22,

                    boxShadow:
                        "0 12px 40px rgba(0,0,0,.35)",

                    transition: "all .25s ease",

                    "&:hover": {
                        transform: "translateY(-2px)",
                        boxShadow:
                            "0 18px 50px rgba(0,0,0,.45)",
                    },
                },
            },
        },

        MuiPaper: {
            styleOverrides: {
                root: {
                    backgroundImage: "none",
                },
            },
        },

        MuiDrawer: {
            styleOverrides: {
                paper: {
                    background: "rgba(16,24,46,.82)",

                    backdropFilter: "blur(24px)",

                    borderRight:
                        "1px solid rgba(255,255,255,.06)",
                },
            },
        },

        MuiAppBar: {
            styleOverrides: {
                root: {
                    background: "rgba(9,12,21,.75)",

                    backdropFilter: "blur(24px)",

                    boxShadow: "none",

                    borderBottom:
                        "1px solid rgba(255,255,255,.05)",
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