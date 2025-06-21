document.addEventListener("DOMContentLoaded", function () {
  const uploadForm = document.getElementById("uploadForm");
  const assignmentInput = document.getElementById("assignment");
  const downloadBtn = document.getElementById("downloadResults");

  uploadForm.addEventListener("submit", async function (e) {
    e.preventDefault();
    const file = assignmentInput.files[0];
    if (!file) return alert("Please upload a file.");

    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await fetch("http://127.0.0.1:8002/upload-assignment", {
        method: "POST",
        body: formData,
      });

      const data = await res.json();
      alert(data.message || "Uploaded successfully.");
    } catch (err) {
      alert("Upload failed.");
      console.error(err);
    }
  });

  downloadBtn.addEventListener("click", async function () {
    try {
      const res = await fetch("http://127.0.0.1:8002/export-results");
      if (!res.ok) throw new Error("Download failed");

      const blob = await res.blob();
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = "assignment_results.pdf";
      a.click();
      window.URL.revokeObjectURL(url);
    } catch (err) {
      alert("Error downloading PDF.");
      console.error(err);
    }
  });
});
