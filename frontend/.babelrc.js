const plugins = [
    [
        // Config for babel-plugin-import which allows easier importing of Material UI components: https://material-ui.com/guides/minimizing-bundle-size/
        "babel-plugin-import",
        {
            libraryName: "@material-ui/core",
            // Use "'libraryDirectory': ''," if your bundler does not support ES modules
            libraryDirectory: "esm",
            camel2DashComponentName: false,
        },
        "core",
    ],
    [
        "babel-plugin-import",
        {
            libraryName: "@material-ui/icons",
            // Use "'libraryDirectory': ''," if your bundler does not support ES modules
            libraryDirectory: "esm",
            camel2DashComponentName: false,
        },
        "icons",
    ],
];

module.exports = { plugins };
