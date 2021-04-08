import { makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles((theme) => ({
    title: {
        "font-size": 74,
        "font-family": "SignPainter, Roboto",
        "text-shadow": "1px 4px #000000",
    },
    subtitle: {
        "font-weight": 500,
        color: theme.palette.text.hint,
    },
    paper: {
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        width: "30em",
    },
    container: {
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        "padding-top": "10em",
    },
    avatar: {
        margin: theme.spacing(1),
        backgroundColor: theme.palette.secondary.main,
    },
    form: {
        width: "100%", // Fix IE 11 issue.
        marginTop: theme.spacing(1),
    },
    submit: {
        margin: theme.spacing(3, 0, 2),
    },
}));

export default useStyles;
