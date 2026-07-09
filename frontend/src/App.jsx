import { BrowserRouter, Routes, Route } from "react-router-dom";
import { Suspense, lazy } from "react";

const Dashboard = lazy(() => import("./pages/Dashboard"));
const Gestures = lazy(() => import("./pages/Gestures"));
const Actions = lazy(() => import("./pages/Actions"));
const Training = lazy(() => import("./pages/Training"));
const Analytics = lazy(() => import("./pages/Analytics"));
const Settings = lazy(() => import("./pages/Settings"));

function LoadingScreen() {

    return (

        <div
            style={{
                width: "100vw",
                height: "100vh",
                display: "flex",
                justifyContent: "center",
                alignItems: "center",
                background: "#050B18",
                color: "#ffffff",
                fontSize: "22px",
                fontWeight: 600,
            }}
        >
            Loading Gesture Control System...
        </div>

    );

}

export default function App() {

    return (

        <BrowserRouter>

            <Suspense fallback={<LoadingScreen />}>

                <Routes>

                    <Route
                        path="/"
                        element={<Dashboard />}
                    />

                    <Route
                        path="/gestures"
                        element={<Gestures />}
                    />

                    <Route
                        path="/actions"
                        element={<Actions />}
                    />

                    <Route
                        path="/training"
                        element={<Training />}
                    />

                    <Route
                        path="/analytics"
                        element={<Analytics />}
                    />

                    <Route
                        path="/settings"
                        element={<Settings />}
                    />

                </Routes>

            </Suspense>

        </BrowserRouter>

    );

}