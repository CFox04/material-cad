// Standard error message
import React from "react";
import { withTheme } from "@material-ui/core/styles";

class ErrorBoundaryRaw extends React.Component {
    constructor(props) {
        super(props);
        this.state = { hasError: false, error: null };
        this.divStyle = {
            height: "90%",
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            justifyContent: "center",
            color: props.theme.palette.grey["500"],
        };
        this.errorStyle = {
            padding: "0.5em",
            color: props.theme.palette.error.main,
        };
    }

    static getDerivedStateFromError(error) {
        // Update state so the next render will show the fallback UI.
        return { error: error };
    }

    render() {
        if (this.state.error) {
            // You can render any custom fallback UI
            return (
                <div style={this.divStyle}>
                    <h2 style={this.errorStyle}>Something went wrong.</h2>
                    <p>
                        {this.state.error.name}: {this.state.error.message}
                    </p>
                </div>
            );
        }

        return this.props.children;
    }
}

const ErrorBoundary = withTheme(ErrorBoundaryRaw);

export default ErrorBoundary;
