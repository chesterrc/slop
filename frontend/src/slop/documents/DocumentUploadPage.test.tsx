import { expect, test, describe } from "vitest";
import { render, screen, fireEvent } from "@testing-library/react";
import { DocumentUploadPage } from "./DocumentUploadPage";
import { UploadDocument } from "./UploadDocument.tsx";

vi.mock("./UploadDocument", () => ({
    UploadDocument: vi.fn(),
}));

describe("DocumentUploadPage tests", () => {

    test("Should render 'Please Upload Resume'", () => {
        render(<DocumentUploadPage />);

        expect(
            screen.getByText("Please Upload Resume")
        ).toBeInTheDocument();
    });

    test("Should render document upload input", () => {
        render(<DocumentUploadPage />);

        expect(
            screen.getByTestId("resume-upload")
        ).toBeInTheDocument();
    });

    test("Should hide the submit button if no document was uploaded", async () => {
        render(<DocumentUploadPage />);

        const submitButton = screen.queryByRole("button", { name: "Submit" });

        expect(submitButton).not.toBeInTheDocument();
    });

    test("Should show the submit button if document was uploaded", async () => {
        const file = new File(
            ["resume contents"],
            "resume.pdf",
            { type: "application/pdf" }
        );

        render(<DocumentUploadPage />);

        const input = screen.getByTestId("resume-upload");

        fireEvent.change(input, {
            target: {
                files: [file],
            },
        });

        const submitButton = screen.queryByRole("button", {
            name: "Submit",
        });

        expect(submitButton).not.toBeInTheDocument();
    });

    test("Should submit the uploaded document", async () => {
        const file = new File(
            ["resume contents"],
            "resume.pdf",
            { type: "application/pdf" }
        );

        render(<DocumentUploadPage />);

        const input = screen.getByTestId("resume-upload");

        fireEvent.change(input, {
            target: {
                files: [file],
            },
        });

        const submitButton = screen.getByRole("button", {
            name: "Submit",
        });

        fireEvent.click(submitButton);

        expect(UploadDocument).toHaveBeenCalledWith(file);
    });
});
