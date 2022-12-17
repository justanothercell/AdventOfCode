use std::collections::HashMap;
use std::fs::File;
use std::io::{BufRead, BufReader};
use itertools::Itertools;

#[derive(Debug)]
struct Valve {
    flow: i32,
    conns: Vec<String>,
}

type Valves = HashMap<String, Valve>;
type ValvePaths = HashMap<String, HashMap<String, i32>>;

fn main() {
    let mut valves = HashMap::new();
    let mut valve_paths = HashMap::new();

    //let file = File::open("../test_input.txt").unwrap();
    // ["JJ", "BB", "CC", "II", "GG"] ["DD", "HH", "EE", "FF", "AA"]: (81, 1707)

    let file = File::open("../input.txt").unwrap();
    let reader = BufReader::new(file);
    for tunnel in reader.lines() {
        let tunnel = tunnel.unwrap();
        let parts: Vec<&str> = tunnel.split(" ").collect();
        let valve = parts[1];
        let flow = parts[4][5..parts[4].len() - 1].parse::<i32>().unwrap();
        let conns = parts[9..].iter().map(|s| s.trim_end_matches(',').to_string()).collect();
        let v = Valve { flow, conns };
        println!("{}: {:?}", valve, v);
        valves.insert(valve.to_string(), v);
    }

    for (name, _valve) in &valves {
        let mut paths = HashMap::new();
        apply_connection(name, name, &valves, &mut paths, 0);
        valve_paths.insert(name.to_string(), paths);
    }
    println!();
    for (name, paths) in &valve_paths {
        let paths: HashMap<String, i32> = paths
            .iter()
            .filter(|(k, _)| valves[*k].flow != 0)
            .map(|(k, v)| (k.to_string(), *v))
            .collect();
        println!("{}: {:?}", name, paths);
    }
    println!();
    let mut max_flow = (0, 0);
    let tasks = valve_paths["AA"].keys().cloned().collect::<Vec<String>>();
    let total = factorial(tasks.len() as u64);
    for (i, arrangement) in tasks.iter().permutations(tasks.len()).enumerate() {
        let midpoint = arrangement.len() / 2;
        let (m_tasks, e_tasks) = arrangement.split_at(midpoint);
        let (m_path, e_path, flow, total_flow) = simulate(&valves, &valve_paths, m_tasks, e_tasks);
        if total_flow > max_flow.1 {
            max_flow = (flow, total_flow);
            println!("{m_path:?} {e_path:?}: {max_flow:?}");
        }
        if i % 1000000 == 0 {
            println!("{}", i as f32 / total as f32)
        }
    }
    println!();
    println!("{max_flow:?}");
}

fn apply_connection(start: &str, end: &str, valves: &Valves, paths: &mut HashMap<String, i32>, length: i32) {
    if !paths.contains_key(end) || paths[end] > length {
        paths.insert(end.to_string(), length);
        for conn in &valves[end].conns {
            apply_connection(start, conn, valves, paths, length + 1);
        }
    }
}

fn simulate<'a>(valves: &'a Valves, valve_paths: &'a ValvePaths, mut m_tasks: &'a [&'a String], mut e_tasks: &'a [&'a String]) -> (Vec<&'a String>, Vec<&'a String>, i32, i32) {
    let mut m_pos = "AA";
    let mut m_d = 0;
    let mut m_path = Vec::new();

    let mut e_pos = "AA";
    let mut e_d = 0;
    let mut e_path = Vec::new();

    let mut flow = 0;
    let mut total_flow = 0;
    let mut time = 0;

    while time < 26 {
        if !m_tasks.is_empty() {
            if m_d == 0 {
                flow += valves[m_pos].flow;
                let dest = m_tasks[0];
                m_d = valve_paths[m_pos][dest] + 1;
                m_pos = dest;
                m_path.push(dest);
                m_tasks = &m_tasks[1..];
            }
        } else {
            if m_d == 0 {
                flow += valves[m_pos].flow;
            }
        }
        if !e_tasks.is_empty() {
            if e_d == 0 {
                flow += valves[e_pos].flow;
                let dest = e_tasks[0];
                e_d = valve_paths[e_pos][dest] + 1;
                e_pos = dest;
                e_path.push(dest);
                e_tasks = &e_tasks[1..];
            }
        } else {
            if e_d == 0 {
                flow += valves[e_pos].flow;
            }
        }
        m_d -= 1;
        e_d -= 1;
        total_flow += flow;
        time += 1;
    }
    (m_path, e_path, flow, total_flow)
}

fn factorial(n: u64) -> u64 {
    if n == 0 { 1 } else { n * factorial(n - 1) }
}