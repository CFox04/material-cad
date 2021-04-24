import React, { useState } from "react";
import { Box } from "@material-ui/core";
import { makeStyles, withTheme } from "@material-ui/core/styles";
import { useHistory } from "react-router-dom";

const useStyles = makeStyles((theme) => ({
    image: {
        width: "55%",
        height: "55%",
        padding: "0.3em",
    },
    box: {
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        margin: "2.5em",
        width: "10em",
        height: "10em",
        boxShadow: theme.shadows[1],
        color: theme.palette.text.hint,
        backgroundColor: theme.palette.background.paper,
    },
}));

function Card(props) {
    const history = useHistory();
    const [hover, setHover] = useState(false);

    const classes = useStyles();

    const hoverColor = props.theme.palette.primary.main;
    const disabledColor = props.theme.palette.disabled;

    function getImageColor() {
        if (!props.disabled) {
            if (hover && !props.disabled) {
                return hoverColor;
            } else {
                return "white";
            }
        } else {
            return disabledColor;
        }
    }

    function getTextColor() {
        if (!props.disabled) {
            if (hover && !props.disabled) {
                return { color: hoverColor };
            } else {
                return { color: props.theme.palette.text.hint };
            }
        } else {
            return { color: disabledColor };
        }
    }

    return (
        <Box
            className={classes.box}
            onMouseEnter={() => setHover(true)}
            onMouseLeave={() => setHover(false)}
            style={
                props.disabled ? { cursor: "default" } : { cursor: "pointer" }
            }
            onClick={() => {
                if (props.href) {
                    history.push(props.href);
                }
            }}
        >
            {<props.img fill={getImageColor()} className={classes.image} />}
            <span style={getTextColor()}>{props.children}</span>
        </Box>
    );
}

export default withTheme(Card);
