import React from "react";
import "../App.css";
import CardComponent from "../components/NewStackCard";

export default function CreateStack() {
    return (
        <div className="myStackpage pt-2">
            <div className="mx-auto max-w-7xl px-2 sm:px-6 lg:px-8 myStackDiv">
                <div className="relative flex h-16 items-center justify-between">
                    <div className="flex flex-1 items-center sm:items-stretch sm:justify-start">
                        <div className="flex flex-shrink-0">
                            <h1 className="myStackHead">My Stacks</h1>
                        </div>
                    </div>
                    <div className="absolute inset-y-0 right-0 flex items-center pr-2 sm:static sm:inset-auto sm:ml-6 sm:pr-0">
                        <button className="newStackButton"><span className="plusIcon">+</span> New Stack</button>
                    </div>
                </div>
            </div>
            <CardComponent />
        </div>
    )
}