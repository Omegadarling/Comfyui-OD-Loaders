import { app } from "../../scripts/app.js";
import { ComfyWidgets } from "../../scripts/widgets.js";

app.registerExtension({
    name: "pysssss.od_lora",
    async beforeRegisterNodeDef(nodeType, nodeData, app) {
        if (nodeData.name === "OD_LoraLoader") {
            const onNodeCreated = nodeType.prototype.onNodeCreated;
            nodeType.prototype.onNodeCreated = function() {
                const r = onNodeCreated?.apply(this, arguments);

                const widget = this.widgets.find(w => w.name === "lora_name");
                if (!widget) return r;

                widget.showMenu = () => {
                    const options = [];
                    if (widget.value?.image || widget.value?.content) {
                        options.push({
                            content: "View Lora info...",
                            callback: () => {
                                const name = widget.value?.content || widget.value;
                                if (name) {
                                    fetch(`/pysssss/examples/loras/${name}`)
                                        .then(response => response.json())
                                        .then(examples => {
                                            const prefix = `loras/${name.replace(/\.[^/.]+$/, "")}`;
                                            const popupDiv = document.createElement("div");
                                            popupDiv.style.position = "absolute";
                                            popupDiv.style.zIndex = 10000;

                                            const img = document.createElement("img");
                                            img.src = `/pysssss/view/${prefix}.preview.png`;
                                            img.style.maxWidth = "512px";
                                            img.style.maxHeight = "512px";
                                            popupDiv.appendChild(img);

                                            if (examples?.length) {
                                                const textarea = document.createElement("textarea");
                                                textarea.style.width = "512px";
                                                textarea.style.height = "300px";
                                                fetch(`/pysssss/view/${prefix}.txt`)
                                                    .then(response => response.text())
                                                    .then(text => textarea.value = text);
                                                popupDiv.appendChild(textarea);
                                            }

                                            const closeBtn = document.createElement("button");
                                            closeBtn.textContent = "Close";
                                            closeBtn.onclick = () => popupDiv.remove();
                                            popupDiv.appendChild(closeBtn);

                                            document.body.appendChild(popupDiv);
                                            const rect = this.getBoundingClientRect();
                                            popupDiv.style.left = rect.left + "px";
                                            popupDiv.style.top = rect.bottom + "px";
                                        });
                                }
                            }
                        });
                    }
                    return options;
                };

                return r;
            };
        }
    }
});