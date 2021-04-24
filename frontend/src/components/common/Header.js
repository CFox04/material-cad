import React from "react";
import { makeStyles, Box } from "@material-ui/core";
import IconButton from "@material-ui/core/IconButton";
import ExitToAppIcon from "@material-ui/icons/ExitToAppSharp";
import HomeSharpIcon from "@material-ui/icons/HomeSharp";

const useStyles = makeStyles((theme) => ({
    box: {
        position: "relative",
        width: "100%",
        padding: "2em 0",
    },
    icon: {
        // position: "absolute",
        color: theme.palette.text.hint,
        cursor: "pointer",
        padding: "none",
    },
    input: {
        display: "none",
    },
}));

function Header() {
    const classes = useStyles();

    return (
        <Box
            display="flex"
            flexDirection="row"
            justifyContent="space-between"
            className={classes.box}
        >
            <IconButton aria-label="home" size="small" href="/">
                <HomeSharpIcon className={classes.icon} fontSize="small" />
            </IconButton>
            <IconButton aria-label="sign out" size="small" href="/logout">
                <ExitToAppIcon className={classes.icon} fontSize="small" />
            </IconButton>
        </Box>
    );
}

export default Header;
