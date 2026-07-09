import React from "react";
import ReactDOM from "react-dom/client";

import { CssBaseline, ThemeProvider } from "@mui/material";
import { Toaster } from "react-hot-toast";

import App from "./App";
import theme from "./theme/theme";

import "./index.css";

ReactDOM.createRoot(document.getElementById("root")).render(

    <React.StrictMode>

        <ThemeProvider theme={theme}>

            <CssBaseline/>

            <App/>

            <Toaster
                position="bottom-right"
                toastOptions={{
                    duration:3000,
                }}
            />

        </ThemeProvider>

    </React.StrictMode>

);