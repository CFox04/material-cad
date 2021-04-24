// Button that
import React, { useState } from "react";
import { Button } from "@material-ui/core";
import { withTheme } from "@material-ui/core/styles";
import onSoundPath from "../../sounds/toggle.mp3";
import offSoundPath from "../../sounds/untoggle.mp3";

// Create audio objects
let onSound = new Audio(onSoundPath);
let offSound = new Audio(offSoundPath);

function ToggleButton(props) {
    const [toggled, Toggle] = useState(false);

    const colorMapping = {
        warning: props.theme.palette.warning.main,
        danger: props.theme.palette.error.main,
        success: props.theme.palette.success.main,
        primary: props.theme.palette.primary.main,
        secondary: props.theme.palette.secondary.main,
    };

    // Get style depending on state and color property
    function getStyle() {
        // If a valid color was passed in to properties
        if (colorMapping[props.color]) {
            if (!toggled) {
                return {
                    color: colorMapping[props.color],
                };
            }

            return {
                backgroundColor: colorMapping[props.color],
            };
        }

        return {
            color: colorMapping[props.color],
        };
    }

    const { color, variant, onClick, style, children, ...attributes } = props;

    return (
        <Button
            color="default"
            variant={toggled ? "contained" : "outlined"}
            onClick={() => {
                Toggle(!toggled);
                toggled ? offSound.play() : onSound.play();
                // Run any other code passed to onClick through props
                if (typeof props.onClick === "function") {
                    props.onClick();
                }
            }}
            style={getStyle()}
            {...attributes}
        >
            {props.children}
        </Button>
    );
}

export default withTheme(ToggleButton);
