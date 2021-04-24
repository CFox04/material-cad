import React from "react";
import { Link } from "@material-ui/core";
import { makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles((theme) => ({
    div: {
        height: "90%",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        color: theme.palette.grey["500"],
    },
    error: {
        padding: "0.5em",
        color: theme.palette.error.main,
    },
}));

function NotFound() {
    const classes = useStyles();

    return (
        <div className={classes.div}>
            <h2 className={classes.error}>404 - Page not found!</h2>
            {/* <p>
                {this.state.error.name}: {this.state.error.message}
            </p> */}
            <Link href="/">Return home</Link>
        </div>
    );
}

export default NotFound;
