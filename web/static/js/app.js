async function loadHardware() {
  try {
    // Solicita os dados ao endpoint da API
    const response = await fetch("/api/hardware");

    // Verifica se a requisição foi bem-sucedida
    if (!response.ok) {
      throw new Error("Falha ao consultar hardware");
    }

    // Converte a resposta JSON em um objeto JavaScript
    const hardware = await response.json();

    // Separa as informações da CPU
    const cpu = hardware.cpu;

    // Atualiza os elementos HTML
    document.getElementById("cpu-usage").textContent =
      `${Number(cpu.cpu_usage).toFixed(1)}%`;

    document.getElementById("cpu-model").textContent = cpu.model;
  } catch (error) {
    console.error("Erro ao carregar hardware:", error);

    document.getElementById("cpu-usage").textContent = "Erro";

    document.getElementById("cpu-model").textContent =
      "Não foi possível consultar a CPU";
  }
}

function formatBytes(bytes) {
  const units = ["B", "KiB", "MiB", "GiB", "TiB"];

  if (bytes === 0) return "0 B";

  const exponent = Math.min(
    Math.floor(Math.log(bytes) / Math.log(1024)),
    units.length - 1,
  );

  const value = bytes / Math.pow(1024, exponent);

  return `${value.toFixed(1)} ${units[exponent]}`;
}

async function loadHardware() {
  try {
    const response = await fetch("/api/hardware");

    if (!response.ok) {
      throw new Error("Falha ao consultar hardware");
    }

    const hardware = await response.json();

    // CPU
    const cpu = hardware.cpu;

    document.getElementById("cpu-usage").textContent =
      `${Number(cpu.cpu_usage).toFixed(1)}%`;

    document.getElementById("cpu-model").textContent = cpu.model;

    // RAM
    const ram = hardware.ram;

    document.getElementById("ram-usage").textContent =
      `${Number(ram.memory_percent).toFixed(1)}%`;

    document.getElementById("ram-details").textContent =
      `${formatBytes(ram.used_memory)} usados de ${formatBytes(ram.memory_quantity)}`;

    // ARMAZENAMENTO
    const disks = hardware.disk;

    document.getElementById("disk-count").textContent =
      `${disks.length} ${disks.length === 1 ? "unidade" : "unidades"}`;

    document.getElementById("disk-details").textContent = disks
      .map((disk) => `${disk.device} ${Number(disk.percent).toFixed(1)}% usado`)
      .join(" | ");
  } catch (error) {
    console.error("Erro ao carregar hardware:", error);
  }
}

loadHardware();
