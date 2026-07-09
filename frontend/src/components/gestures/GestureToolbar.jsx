import {
    Stack,
    TextField,
    InputAdornment,
    Chip,
    IconButton,
    Tooltip,
    MenuItem,
} from "@mui/material";

import SearchRoundedIcon from "@mui/icons-material/SearchRounded";
import RefreshRoundedIcon from "@mui/icons-material/RefreshRounded";
import SortRoundedIcon from "@mui/icons-material/SortRounded";

import { motion } from "framer-motion";

export default function GestureToolbar({

    search,

    setSearch,

    filter,

    setFilter,

    sort,

    setSort,

    refresh,

}) {

    const filters = [
        "All",
        "Active",
        "Inactive",
    ];

    return (

        <motion.div

            initial={{
                opacity: 0,
                y: 20,
            }}

            animate={{
                opacity: 1,
                y: 0,
            }}

            transition={{
                duration: .45,
            }}

        >

            <Stack

                direction={{
                    xs: "column",
                    md: "row",
                }}

                spacing={2}

                alignItems={{
                    xs: "stretch",
                    md: "center",
                }}

                justifyContent="space-between"

                sx={{
                    mb: 4,
                }}

            >

                {/* Search */}

                <TextField

                    value={search}

                    onChange={(e) =>
                        setSearch(e.target.value)
                    }

                    placeholder="Search gestures..."

                    sx={{
                        width: {
                            xs: "100%",
                            md: 360,
                        },

                        "& .MuiOutlinedInput-root": {

                            borderRadius: 4,

                            bgcolor: "rgba(255,255,255,.03)",

                            transition: ".25s",

                            "&:hover": {

                                bgcolor: "rgba(255,255,255,.05)",

                            },

                            "&.Mui-focused": {

                                boxShadow:
                                    "0 0 0 3px rgba(99,102,241,.18)",

                            },

                        },

                    }}

                    InputProps={{

                        startAdornment: (

                            <InputAdornment position="start">

                                <SearchRoundedIcon
                                    color="primary"
                                />

                            </InputAdornment>

                        ),

                    }}

                />

                {/* Controls */}

                <Stack

                    direction="row"

                    spacing={1.5}

                    alignItems="center"

                    flexWrap="wrap"

                >

                    {

                        filters.map((item) => (

                            <Chip

                                key={item}

                                label={item}

                                clickable

                                color={
                                    filter === item
                                        ? "primary"
                                        : "default"
                                }

                                onClick={() =>
                                    setFilter(item)
                                }

                                sx={{

                                    fontWeight: 600,

                                    transition: ".25s",

                                    "&:hover": {

                                        transform:
                                            "translateY(-2px)",

                                    },

                                }}

                            />

                        ))

                    }

                    <TextField

                        select

                        size="small"

                        value={sort}

                        onChange={(e) =>
                            setSort(e.target.value)
                        }

                        sx={{

                            minWidth: 180,

                            "& .MuiOutlinedInput-root": {

                                borderRadius: 3,

                            },

                        }}

                        InputProps={{

                            startAdornment: (

                                <InputAdornment position="start">

                                    <SortRoundedIcon
                                        fontSize="small"
                                    />

                                </InputAdornment>

                            ),

                        }}

                    >

                        <MenuItem value="name">

                            Name

                        </MenuItem>

                        <MenuItem value="accuracy">

                            Accuracy

                        </MenuItem>

                        <MenuItem value="samples">

                            Dataset Size

                        </MenuItem>

                    </TextField>

                    <Tooltip title="Refresh">

                        <IconButton

                            color="primary"

                            onClick={refresh}

                            sx={{

                                width: 46,

                                height: 46,

                                bgcolor:
                                    "rgba(99,102,241,.12)",

                                transition: ".25s",

                                "&:hover": {

                                    bgcolor:
                                        "rgba(99,102,241,.25)",

                                    transform:
                                        "rotate(180deg)",

                                },

                            }}

                        >

                            <RefreshRoundedIcon />

                        </IconButton>

                    </Tooltip>

                </Stack>

            </Stack>

        </motion.div>

    );

}