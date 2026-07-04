import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";

import Dashboard from "./pages/Dashboard";
import Gestures from "./pages/Gestures";
import Actions from "./pages/Actions";
import Training from "./pages/Training";
import Analytics from "./pages/Analytics";
import Settings from "./pages/Settings";

function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Navigate to="/dashboard" replace />} />

                <Route path="/dashboard" element={<Dashboard />} />
                <Route path="/gestures" element={<Gestures />} />
                <Route path="/actions" element={<Actions />} />
                <Route path="/training" element={<Training />} />
                <Route path="/analytics" element={<Analytics />} />
                <Route path="/settings" element={<Settings />} />
            </Routes>
        </BrowserRouter>
    );
}

export default App;