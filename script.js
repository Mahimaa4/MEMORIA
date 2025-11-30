// Upload PDF and store embeddings
async function uploadPDF(){
    const fileInput = document.getElementById("pdfFile");
    const file = fileInput.files[0];
    if(!file) return alert("Upload a PDF first!");

    const formData = new FormData();
    formData.append("file", file);

    const uploadStatus = document.getElementById("uploadStatus");
    uploadStatus.innerText = "📄 Processing PDF...";

    try {
        const res = await fetch("/process_pdf", { method: "POST", body: formData });
        const data = await res.json();

        if(data.status==="success"){
            uploadStatus.innerText = `✅ Uploaded! ${data.chunks_stored} chunks embedded.`;
        } else {
            uploadStatus.innerText = `❌ Upload failed: ${data.msg || "Unknown error"}`;
        }
    } catch(err) {
        uploadStatus.innerText = `❌ Error: ${err}`;
    }
}

// Send chat query to backend
async function sendChat(){
    const input = document.getElementById("userMsg");
    const msg = input.value.trim();
    if(!msg) return;

    const responseBox = document.getElementById("responseBox");
    responseBox.innerText = "⏳ Retrieving answer...";

    try {
        const res = await fetch("/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ query: msg })  // ✅ Use 'query' for backend
        });
        const data = await res.json();
        responseBox.innerText = data.answer || "❌ No answer returned";
    } catch(err) {
        responseBox.innerText = `❌ Error: ${err}`;
    }

    input.value = "";
}
