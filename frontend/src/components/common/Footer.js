import React from "react";
import { Typography, Link, makeStyles } from "@material-ui/core";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faDiscord } from "@fortawesome/free-brands-svg-icons";

const useStyles = makeStyles((theme) => ({
    div: {
        position: "absolute",
        width: "100%",
        bottom: 0,
        padding: "2em 0",
        verticalAlign: "middle",
    },
    text: {
        position: "relative",
        color: theme.palette.text.hint,
        width: "100%",
    },
    icon: {
        position: "absolute",
        fontSize: "1.5em",
        marginTop: "0.25em",
        color: theme.palette.text.hint,
        cursor: "pointer",
        left: 0,
    },
}));

function Footer() {
    const classes = useStyles();

    return (
        <div className={classes.div}>
            <Typography className={classes.text} variant="body2" align="center">
                <Link
                    rel="noopener"
                    href="https://discord.gg/qsyFThqper"
                    target="_blank"
                >
                    <FontAwesomeIcon
                        icon={faDiscord}
                        className={classes.icon}
                    />
                </Link>
                {"Copyright © "}
                <Link color="inherit" href="#">
                    Sunnyvale Roleplay
                </Link>{" "}
                {new Date().getFullYear()}
                {"."}
            </Typography>
        </div>
    );
}

export default Footer;
