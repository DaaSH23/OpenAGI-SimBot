import { useContext } from 'react';
import { Dialog, DialogPanel, DialogTitle, Transition, TransitionChild } from '@headlessui/react';
import { AppContext } from '../utils/AppContext';
import "../App.css"

export default function NewStackFormPop() {
    const { open, setOpen } = useContext(AppContext);

    return (
        <Transition show={open}>
            <Dialog className="relative z-10" onClose={() => setOpen(false)}>
                <TransitionChild
                    enter="ease-out duration-300"
                    enterFrom="opacity-0"
                    enterTo="opacity-100"
                    leave="ease-in duration-200"
                    leaveFrom="opacity-100"
                    leaveTo="opacity-0"
                >
                    <div className="fixed inset-0 bg-gray-500 bg-opacity-75 transition-opacity" />
                </TransitionChild>

                <div className="fixed inset-0 z-10 w-full overflow-y-auto">
                    <div className="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
                        <TransitionChild
                            enter="ease-out duration-300"
                            enterFrom="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
                            enterTo="opacity-100 translate-y-0 sm:scale-100"
                            leave="ease-in duration-200"
                            leaveFrom="opacity-100 translate-y-0 sm:scale-100"
                            leaveTo="opacity-0 translate-y-4 sm:translate-y-0 sm:scale-95"
                        >
                            <DialogPanel className="relative transform overflow-hidden rounded-lg bg-white text-left shadow-xl transition-all w-full sm:my-8 sm:max-w-lg">
                                <div className="bg-white px-4 pb-4 pt-5 sm:p-6 sm:pb-4 w-full">
                                    <div className="sm:flex sm:items-start w-full">
                                        <div className="mt-3 text-left  sm:mt-0 w-full">
                                            <DialogTitle as="h3" className="text-base font-bold leading-6 text-gray-900 DialogTitle">
                                                Create New Stack
                                            </DialogTitle>
                                            <div className="mt-4 w-full">
                                                <div>
                                                    <label htmlFor="name" className="block text-sm font-medium text-gray-700">
                                                        Name
                                                    </label>
                                                    <input
                                                        type="text"
                                                        name="name"
                                                        id="name"
                                                        className="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm cardtextArea"
                                                    />
                                                </div>
                                                <div className="mt-4">
                                                    <label htmlFor="description" className="block text-sm font-medium text-gray-700">
                                                        Description
                                                    </label>
                                                    <textarea
                                                        name="description"
                                                        id="description"
                                                        rows={3}
                                                        className="mt-1 w-full rounded-md  shadow-sm sm:text-sm cardtextArea"
                                                        defaultValue={""}
                                                    />
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div className="bg-gray-50 px-4 py-3 sm:flex sm:flex-row-reverse sm:px-6 w-full">
                                    <button
                                        type="button"
                                        className="inline-flex justify-center w-full rounded-md  px-3 py-2 text-sm font-semibold text-white shadow-sm sm:ml-3 sm:w-auto createButton"
                                        onClick={() => setOpen(false)}
                                    >
                                        Create
                                    </button>
                                    <button
                                        type="button"
                                        className="mt-3 inline-flex w-full justify-center rounded-md bg-white px-3 py-2 text-sm font-semibold text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 hover:bg-gray-50 sm:mt-0 sm:w-auto"
                                        onClick={() => setOpen(false)}
                                    >
                                        Cancel
                                    </button>
                                </div>
                            </DialogPanel>
                        </TransitionChild>
                    </div>
                </div>
            </Dialog>
        </Transition>
    );
}
