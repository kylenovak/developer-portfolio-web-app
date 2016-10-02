import * as React from "react";

export interface HelloProps { compiler: string; framework: string; }

export default class Hello extends React.Component<HelloProps, {}> {
    constructor(props: HelloProps) {
        super(props);
    }

    public render() {
        return (
            <h1>Hello from 123 {this.props.compiler} and {this.props.framework}!</h1>
        );
    }
}