import React from "react";
import { Visibility, VisibilityOff } from "@material-ui/icons";
import { TextField, IconButton, InputAdornment } from "@material-ui/core";

const defaultProps = {
    variant: "filled",
    margin: "normal",
    required: true,
    fullWidth: true,
    id: "password",
    label: "Password",
    name: "password",
    autoComplete: "current-password",
    autoFocus: true,
};

function PasswordField({ textFieldProps }) {
    const [password, setPassword] = React.useState({
        value: "",
        visible: false,
    });

    const handleClickShowPassword = () => {
        setPassword({ ...password, visible: !password.visible });
    };

    const handleMouseDownPassword = (event) => {
        event.preventDefault();
    };

    // If user passed in props for input field, deny them
    if (textFieldProps["InputProps"]) {
        console.log("Warning: Cannot specify InputProps for PasswordField.");
        delete textFieldProps["InputProps"];
    }

    for (let prop in defaultProps) {
        if (!textFieldProps[prop]) {
            textFieldProps[prop] = defaultProps[prop];
        }
    }

    return (
        <TextField
            {...textFieldProps}
            InputProps={{
                type: password.visible ? "text" : "password",
                endAdornment: (
                    <InputAdornment position="end">
                        <IconButton
                            aria-label="toggle password visibility"
                            onClick={handleClickShowPassword}
                            onMouseDown={handleMouseDownPassword}
                        >
                            {password.visible ? (
                                <Visibility />
                            ) : (
                                <VisibilityOff />
                            )}
                        </IconButton>
                    </InputAdornment>
                ),
            }}
        />
    );
}

PasswordField.defaultProps = {
    textFieldProps: defaultProps,
};

export default PasswordField;
