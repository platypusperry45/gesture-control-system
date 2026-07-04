import { Chip } from "@mui/material";

const colors = {
    healthy: "success",
    online: "success",
    running: "success",

    warning: "warning",

    stopped: "error",
    offline: "error",

    loading: "info",
};

export default function StatusBadge({
    status,
    label,
}) {
    const color =
        colors[status?.toLowerCase()] || "default";

    return (
        <Chip
            label={label || status}
            color={color}
            size="small"
            sx={{
                fontWeight: 600,
            }}
        />
    );
}