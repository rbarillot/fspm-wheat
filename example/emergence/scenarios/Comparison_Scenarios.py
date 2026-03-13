import os
import pandas as pd
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import numpy as np

delta_t_simuls = 1509
# meteo_data = pd.read_csv(os.path.join('inputs', 'meteo.csv'), index_col='t')
# meteo_data['Date'] = pd.to_datetime(meteo_data['Date'], format='%d/%m/%Y')


def phloem(df_scenarios_dict, tmin, tmax):
    fig, axs = plt.subplots(2, 2)

    # phloem sucrose & AA

    for scenario_num, data in df_scenarios_dict.items():
        df_current_organs = data['organs']
        # 1
        axs[0, 0].plot(df_current_organs[(df_current_organs.organ == 'phloem')]['t'], df_current_organs[(df_current_organs.organ == 'phloem')]['Conc_Sucrose'], label=data['label'])
        # 2
        axs[0, 1].plot(df_current_organs[(df_current_organs.organ == 'phloem')]['t'], df_current_organs[(df_current_organs.organ == 'phloem')]['sucrose'], label=data['label'])
        # 3
        axs[1, 0].plot(df_current_organs[(df_current_organs.organ == 'phloem')]['t'], df_current_organs[(df_current_organs.organ == 'phloem')]['Conc_Amino_Acids'], label=data['label'])
        # 4
        axs[1, 1].plot(df_current_organs[(df_current_organs.organ == 'phloem')]['t'], df_current_organs[(df_current_organs.organ == 'phloem')]['amino_acids'], label=data['label'])

    # 1
    axs[0, 0].set_xlim(tmin, tmax)
    axs[0, 0].set_ylabel('Concentration sucrose (µmol g-1)')

    # 2
    axs[0, 1].set_xlim(tmin, tmax)
    axs[0, 1].set_ylabel('Amount of sucrose (µmol C)')

    # 3
    axs[1, 0].set_xlim(tmin, tmax)
    axs[1, 0].set_ylabel('Concentration amino acids (µmol g-1)')

    # ax2 = axs[1, 0].twiny()
    # ax2.set_xticks(axs[1, 0].get_xticks())
    # ax2.set_xticklabels(meteo_data.loc[axs[1, 0].get_xticks()]['Date'].dt.strftime('%d/%m'))
    # ax2.xaxis.set_ticks_position('bottom')  # set the position of the second x-axis to bottom
    # ax2.xaxis.set_label_position('bottom')  # set the position of the second x-axis to bottom
    # ax2.spines['bottom'].set_position(('outward', 35))

    # 4
    axs[1, 1].legend(fontsize="4")
    axs[1, 1].set_xlim(tmin, tmax)
    axs[1, 1].set_ylabel('amino acids (µmol N)')

    # ax2 = axs[1, 1].twiny()
    # ax2.set_xticks(axs[1, 1].get_xticks())
    # ax2.set_xticklabels(meteo_data.loc[axs[1, 1].get_xticks()]['Date'].dt.strftime('%d/%m'))
    # ax2.xaxis.set_ticks_position('bottom')  # set the position of the second x-axis to bottom
    # ax2.xaxis.set_label_position('bottom')  # set the position of the second x-axis to bottom
    # ax2.spines['bottom'].set_position(('outward', 35))

    plt.tight_layout()
    pdf.savefig()  # saves the current figure into a pdf page
    plt.close()

def photosynthesis(df_scenarios_dict):

    fig, axis = plt.subplots()

    for scenario_num, data in df_scenarios_dict.items():
        df_current_axes = data['axes']
        df_current_axes['day'] = df_current_axes['t'] // 24 + 1
        axis.plot(df_current_axes['day'].unique(), df_current_axes.groupby('day')['Total_Photosynthesis'].sum(), label=data['label'])

    axis.set_xlabel('Time (day)')
    axis.set_ylabel('Total Photosynthesis µmol C')
    axis.legend()

    plt.tight_layout()
    pdf.savefig()  # saves the current figure into a pdf page
    plt.close()

def roots(df_scenarios_dict, tmin, tmax):
    fig, axs = plt.subplots(2, 2)

    # phloem sucrose & AA
    for scenario_num, data in df_scenarios_dict.items():
        df_current_organs = data['organs']
        # 1
        axs[0, 0].plot(df_current_organs[(df_current_organs.organ == 'roots')]['t'], df_current_organs[(df_current_organs.organ == 'roots')]['Conc_Sucrose'], label=data['label'])
        # 2
        axs[0, 1].plot(df_current_organs[(df_current_organs.organ == 'roots')]['t'], df_current_organs[(df_current_organs.organ == 'roots')]['sucrose'], label=data['label'])
        # 3
        axs[1, 0].plot(df_current_organs[(df_current_organs.organ == 'roots')]['t'], df_current_organs[(df_current_organs.organ == 'roots')]['Conc_Nitrates'], label=data['label'])
        # 4
        axs[1, 1].plot(df_current_organs[(df_current_organs.organ == 'roots')]['t'], df_current_organs[(df_current_organs.organ == 'roots')]['Conc_cytokinins'], label=data['label'])

    # 1
    axs[0, 0].set_xlim(tmin, tmax)
    axs[0, 0].set_ylabel('Concentration sucrose (µmol g-1)')
    # 2
    axs[0, 1].set_xlim(tmin, tmax)
    axs[0, 1].set_ylim(0, 1000)
    axs[0, 1].set_ylabel('Amount of sucrose (µmol C)')

    # 3
    axs[1, 0].set_xlim(tmin, tmax)
    axs[1, 0].set_ylabel('Concentration nitrates (µmol g-1)')

    # ax2 = axs[1, 0].twiny()
    # ax2.set_xticks(axs[1, 0].get_xticks())
    # ax2.set_xticklabels(meteo_data.loc[axs[1, 0].get_xticks()]['Date'].dt.strftime('%d/%m'))
    # ax2.xaxis.set_ticks_position('bottom')  # set the position of the second x-axis to bottom
    # ax2.xaxis.set_label_position('bottom')  # set the position of the second x-axis to bottom
    # ax2.spines['bottom'].set_position(('outward', 35))

    # 4
    axs[1, 1].legend(fontsize="4")
    axs[1, 1].set_xlim(tmin, tmax)
    axs[1, 1].set_ylabel('Conc_cytokinins (µmol N)')

    # ax2 = axs[1, 1].twiny()
    # ax2.set_xticks(axs[1, 1].get_xticks())
    # ax2.set_xticklabels(meteo_data.loc[axs[1, 1].get_xticks()]['Date'].dt.strftime('%d/%m'))
    # ax2.xaxis.set_ticks_position('bottom')  # set the position of the second x-axis to bottom
    # ax2.xaxis.set_label_position('bottom')  # set the position of the second x-axis to bottom
    # ax2.spines['bottom'].set_position(('outward', 35))

    plt.tight_layout()
    pdf.savefig()  # saves the current figure into a pdf page
    plt.close()

def dry_mass(df_scenarios_dict, tmin, tmax):
    fig, axs = plt.subplots(2, 2, sharex=True)

    for scenario_num, data in df_scenarios_dict.items():
        df_current_axes = data['axes']
        df_current_organs = data['organs']

        # Dry mass shoot
        axs[0, 0].plot(df_current_axes['t'], df_current_axes['sum_dry_mass_shoot'], label=data['label'])
        # Dry mass roots
        axs[0, 1].plot(df_current_axes['t'], df_current_axes['sum_dry_mass_roots'], label=data['label'])
        # mstruct shoot
        axs[1, 0].plot(df_current_axes['t'], df_current_axes['mstruct_shoot'], label=data['label'])
        # mstruct roots
        axs[1, 1].plot(df_current_organs[df_current_organs['organ'] == 'roots']['t'], df_current_organs[df_current_organs['organ'] == 'roots']['mstruct'], label=data['label'])

    # Dry mass shoot
    axs[0, 0].set_xlim(tmin, tmax)
    axs[0, 0].set_ylabel('Dry mass shoot (g)')

    # Dry mass roots
    axs[0, 1].set_xlim(tmin, tmax)
    axs[0, 1].set_ylabel('Dry mass roots (g)')

    # mstruct shoot
    axs[1, 0].set_xlim(tmin, tmax)
    axs[1, 0].set_ylabel('mstruct shoot (g)')

    # ax2 = axs[1, 0].twiny()
    # ax2.set_xticks(axs[1, 0].get_xticks())
    # ax2.set_xticklabels(meteo_data.loc[axs[1, 0].get_xticks()]['Date'].dt.strftime('%d/%m'))
    # ax2.xaxis.set_ticks_position('bottom')  # set the position of the second x-axis to bottom
    # ax2.xaxis.set_label_position('bottom')  # set the position of the second x-axis to bottom
    # ax2.spines['bottom'].set_position(('outward', 35))

    # mstruct roots
    axs[1, 1].legend(fontsize="4")
    axs[1, 1].set_xlim(tmin, tmax)
    axs[1, 1].set_ylabel('mstruct roots (g)')

    # ax2 = axs[1, 1].twiny()
    # ax2.set_xticks(axs[1, 1].get_xticks())
    # ax2.set_xticklabels(meteo_data.loc[axs[1, 1].get_xticks()]['Date'].dt.strftime('%d/%m'))
    # ax2.xaxis.set_ticks_position('bottom')  # set the position of the second x-axis to bottom
    # ax2.xaxis.set_label_position('bottom')  # set the position of the second x-axis to bottom
    # ax2.spines['bottom'].set_position(('outward', 35))
    #

    plt.tight_layout()
    pdf.savefig()  # saves the current figure into a pdf page
    plt.close()


    # shoot : root
    fig, axis = plt.subplots()
    for scenario_num, data in df_scenarios_dict.items():
        df_current_axes = data['axes']
        axis.plot(df_current_axes['t'], df_current_axes['shoot_roots_ratio'], label=data['label'])

    axis.legend()
    axis.set_xlim(tmin, tmax)
    axis.set_ylim(0, 2)
    axis.set_ylabel('shoot : root ratio')

    # ax2 = axis.twiny()
    # ax2.set_xticks(axis.get_xticks())
    # ax2.set_xticklabels(meteo_data.loc[axis.get_xticks()]['Date'].dt.strftime('%d/%m'))
    # ax2.xaxis.set_ticks_position('bottom')  # set the position of the second x-axis to bottom
    # ax2.xaxis.set_label_position('bottom')  # set the position of the second x-axis to bottom
    # ax2.spines['bottom'].set_position(('outward', 35))
    plt.tight_layout()
    pdf.savefig()  # saves the current figure into a pdf page
    plt.close()

def N_mass(df_scenarios_dict, tmin, tmax):
    fig, axs = plt.subplots(2, 2, sharex=True)

    for scenario_num, data in df_scenarios_dict.items():
        df_current_axes = data['axes']
        df_current_organs = data['organs']
        # % N axis
        axs[0, 0].plot(df_current_axes['t'], df_current_axes['N_content'], label=data['label'])
        # N shoot
        axs[0, 1].plot(df_current_axes['t'], df_current_axes['N_content_shoot'], label=data['label'])
        # N axis
        axs[1, 0].plot(df_current_axes['t'], df_current_axes['sum_N_g'], label=data['label'])
        # N uptake
        axs[1, 1].plot(df_current_organs[df_current_organs['organ'] == 'roots']['t'], df_current_organs[df_current_organs['organ'] == 'roots']['Uptake_Nitrates'], label=data['label'])

    # Marion
    # % N axis
    axs[0, 0].set_xlim(tmin, tmax)
    axs[0, 0].set_ylim(0, 10)
    axs[0, 0].set_ylabel('N content axis (% DM)')

    # N shoot
    axs[0, 1].set_xlim(tmin, tmax)
    axs[0, 1].set_ylabel('N content shoot (% DM)')

    # N axis
    axs[1, 0].set_xlim(tmin, tmax)
    axs[1, 0].set_ylabel('N content axis (g)')
    # ax2 = axs[1, 0].twiny()
    # ax2.set_xticks(axs[1, 0].get_xticks())
    # ax2.set_xticklabels(meteo_data.loc[axs[1, 0].get_xticks()]['Date'].dt.strftime('%d/%m'))
    # ax2.xaxis.set_ticks_position('bottom')  # set the position of the second x-axis to bottom
    # ax2.xaxis.set_label_position('bottom')  # set the position of the second x-axis to bottom
    # ax2.spines['bottom'].set_position(('outward', 35))

    # N uptake
    axs[1, 1].legend(fontsize="4")
    axs[1, 1].set_xlim(tmin, tmax)
    axs[1, 1].set_ylabel('Nitrate uptake (µmol)')
    # ax2 = axs[1, 1].twiny()
    # ax2.set_xticks(axs[1, 1].get_xticks())
    # ax2.set_xticklabels(meteo_data.loc[axs[1, 1].get_xticks()]['Date'].dt.strftime('%d/%m'))
    # ax2.xaxis.set_ticks_position('bottom')  # set the position of the second x-axis to bottom
    # ax2.xaxis.set_label_position('bottom')  # set the position of the second x-axis to bottom
    # ax2.spines['bottom'].set_position(('outward', 35))

    plt.tight_layout()
    pdf.savefig()  # saves the current figure into a pdf page
    plt.close()


def surface(df_scenarios_dict, tmin, tmax):
    fig, axs = plt.subplots(2, 2)

    for scenario_num, data in df_scenarios_dict.items():
        df_current_elements = data['elements']

        # Total green area
        axs[0, 0].plot(df_current_elements['t'].unique(), df_current_elements.groupby('t')['green_area'].sum(), label=data['label'])
        # Blade green area
        df_current_elements_blade = df_current_elements[df_current_elements.organ == 'blade']
        axs[0, 1].plot(df_current_elements_blade['t'].unique(), df_current_elements_blade.groupby('t')['green_area'].sum(), label=data['label'])
        # Sheath green area
        df_current_elements_sheath = df_current_elements[df_current_elements.organ == 'sheath']
        axs[1, 0].plot(df_current_elements_sheath['t'].unique(), df_current_elements_sheath.groupby('t')['green_area'].sum(), label=data['label'])
        # Internode green area
        df_current_elements_internode = df_current_elements[df_current_elements.organ == 'internode']
        axs[1, 1].plot(df_current_elements_internode['t'].unique(), df_current_elements_internode.groupby('t')['green_area'].sum(), label=data['label'])

    # Marion
    # Total green area
    axs[0, 0].set_xlim(tmin, tmax)
    axs[0, 0].set_ylabel('Total green area (m²)')

    # Blade green area
    axs[0, 1].set_xlim(tmin, tmax)
    axs[0, 1].set_ylabel('Blade green area (m²)')

    # Sheath green area
    axs[1, 0].set_xlim(tmin, tmax)
    axs[1, 0].set_ylabel('Sheath green area (m²)')
    # ax2 = axs[1, 0].twiny()
    # ax2.set_xticks(axs[1, 0].get_xticks())
    # ax2.set_xticklabels(meteo_data.loc[axs[1, 0].get_xticks()]['Date'].dt.strftime('%d/%m'))
    # ax2.xaxis.set_ticks_position('bottom')  # set the position of the second x-axis to bottom
    # ax2.xaxis.set_label_position('bottom')  # set the position of the second x-axis to bottom
    # ax2.spines['bottom'].set_position(('outward', 35))

    # Internode green area
    axs[1, 1].legend(fontsize=4)
    axs[1, 1].set_xlim(tmin, tmax)
    axs[1, 1].set_ylabel('Internode green area (m²)')
    # ax2 = axs[1, 1].twiny()
    # ax2.set_xticks(axs[1, 1].get_xticks())
    # ax2.set_xticklabels(meteo_data.loc[axs[1, 1].get_xticks()]['Date'].dt.strftime('%d/%m'))
    # ax2.xaxis.set_ticks_position('bottom')  # set the position of the second x-axis to bottom
    # ax2.xaxis.set_label_position('bottom')  # set the position of the second x-axis to bottom
    # ax2.spines['bottom'].set_position(('outward', 35))

    plt.tight_layout()
    pdf.savefig()  # saves the current figure into a pdf page
    plt.close()


def final_dimensions(df_scenarios_dict):
    fig, axs = plt.subplots(2, 2)

    for scenario_num, data in df_scenarios_dict.items():
        df_current_hz = data['hz']
        # Lmax
        axs[0, 0].plot(df_current_hz['metamer'].unique(), df_current_hz.groupby('metamer')['leaf_Lmax'].max(), label=data['label'], marker='o', linestyle='-')
        # Wmax
        axs[0, 1].plot(df_current_hz['metamer'].unique(), df_current_hz.groupby('metamer')['leaf_Wmax'].max(), label=data['label'], marker='o', linestyle='-')
        # SSLW
        axs[1, 0].plot(df_current_hz['metamer'].unique(), df_current_hz.groupby('metamer')['SSLW'].max(), label=data['label'], marker='o', linestyle='-')
        # Phyllochron
        df_current_axes_outputs = data['axes_outputs']
        grouped_df = df_current_hz.groupby('metamer')[['t', 'leaf_is_emerged']]
        leaf_emergence = {}
        for metamer, leaf_E in grouped_df:
            if True not in leaf_E['leaf_is_emerged'].unique():
                continue
            leaf_emergence_t = leaf_E[leaf_E['leaf_is_emerged'] == True].iloc[0]['t']
            leaf_emergence[metamer] = leaf_emergence_t
        phyllochron = {'metamer': [], 'phyllochron': []}
        for metamer, leaf_emergence_t in sorted(leaf_emergence.items()):
            if metamer in (0, 1):
                continue
            phyllochron['metamer'].append(metamer)
            prev_leaf_emergence_t = leaf_emergence[metamer - 1]
            if df_current_axes_outputs[(df_current_axes_outputs['t'] == leaf_emergence_t) | (df_current_axes_outputs['t'] == prev_leaf_emergence_t)].sum_TT.count() == 2:
                phyllo_DD = df_current_axes_outputs[(df_current_axes_outputs['t'] == leaf_emergence_t)].sum_TT.values[0] - df_current_axes_outputs[(df_current_axes_outputs['t'] == prev_leaf_emergence_t)].sum_TT.values[0]
            else:
                phyllo_DD = np.nan
            phyllochron['phyllochron'].append(phyllo_DD)
        axs[1, 1].plot(phyllochron['metamer'], phyllochron['phyllochron'], marker='o', label=data['label'])

    # Lmax
    axs[0, 0].set_ylabel('Final leaf length (m)')
    axs[0, 0].set_xlim(0, 10)
    # Wmax
    axs[0, 1].set_ylabel('Maximal leaf width (m)')
    axs[0, 1].set_xlim(0, 10)
    # SSLW
    axs[1, 0].set_ylabel('Specific Structural leaf weight (g m-2)')
    axs[1, 0].set_xlim(0, 10)
    # Phyllochron
    leaf_emergence = {}
    for metamer, data in grouped_df:
        if metamer == 3 or True not in data['leaf_is_emerged'].unique(): continue
        leaf_emergence_t = data[data['leaf_is_emerged'] == True].iloc[0]['t']
        leaf_emergence[metamer] = leaf_emergence_t

    phyllochron = {'metamer': [], 'phyllochron': []}
    for metamer, leaf_emergence_t in sorted(leaf_emergence.items()):
        if metamer == 4: continue
        phyllochron['metamer'].append(metamer)
        phyllochron['phyllochron'].append(phyllo_DD)

    axs[1, 1].legend(fontsize=4, markerscale=0.5)
    axs[1, 1].set_ylabel('Phyllochron (degree day)')

    plt.tight_layout()
    pdf.savefig()  # saves the current figure into a pdf page
    plt.close()


if __name__ == '__main__':
    scenarios_df = pd.read_csv('scenarios_list.csv')

    df_scenarios_dict = {}
    # get current directory
    path = os.getcwd()

    for scenario_num in scenarios_df['Scenario']:
        df_scenarios_dict[scenario_num] = {}
        df_scenarios_dict[scenario_num]['label'] = scenarios_df[scenarios_df['Scenario'] == scenario_num]['Scenario_label'].iloc[0]

        OUTPUTS = os.path.join(path, 'Scenario_%.4d' % scenario_num, 'outputs')
        POSTPROCESSING = os.path.join(path, 'Scenario_%.4d' % scenario_num, 'postprocessing')
        GRAPHS = os.path.join(path, 'Scenario_%.4d' % scenario_num,)

        # Axes
        df_current_axes = pd.read_csv(os.path.join(POSTPROCESSING, 'axes_postprocessing.csv'))
        df_current_axes = df_current_axes[df_current_axes['axis'] == 'MS']
        df_scenarios_dict[scenario_num]['axes'] = df_current_axes

        df_current_axes_outputs = pd.read_csv(os.path.join(OUTPUTS, 'axes_outputs.csv'))
        df_current_axes_outputs = df_current_axes_outputs[df_current_axes_outputs['axis'] == 'MS']
        df_scenarios_dict[scenario_num]['axes_outputs'] = df_current_axes_outputs

        # Organs
        df_current_organs = pd.read_csv(os.path.join(POSTPROCESSING, 'organs_postprocessing.csv'))
        df_current_organs = df_current_organs[df_current_organs['axis'] == 'MS']
        df_scenarios_dict[scenario_num]['organs'] = df_current_organs

        # Elements
        df_current_elements = pd.read_csv(os.path.join(POSTPROCESSING, 'elements_postprocessing.csv'))
        df_current_elements = df_current_elements[df_current_elements['axis'] == 'MS']
        df_scenarios_dict[scenario_num]['elements'] = df_current_elements

        # HZ
        df_current_hz = pd.read_csv(os.path.join(OUTPUTS, 'hiddenzones_outputs.csv'))
        df_current_hz = df_current_hz[df_current_hz['axis'] == 'MS']
        df_scenarios_dict[scenario_num]['hz'] = df_current_hz

    # # Path Marion
    # dirpath_marion = r'E:\Modeles\Docs\Gauthier_2020_JExpBot\Soumission_JXBot'
    # OUTPUTS_MARION = os.path.join(dirpath_marion, 'outputs')
    # POSTPROCESSING_MARION = os.path.join(dirpath_marion, 'postprocessing')
    # GRAPHS_MARION = os.path.join(dirpath_marion, 'graphs')
    #
    # # Axes
    # df_marion_axes = pd.read_csv(os.path.join(POSTPROCESSING_MARION, 'axes_postprocessing.csv'))
    # df_marion_axes = df_marion_axes[df_marion_axes['axis'] == 'MS']
    # df_marion_axes['t'] = df_marion_axes['t'] + delta_t_simuls
    #
    # # SAMs
    # df_marion_SAMS = pd.read_csv(os.path.join(dirpath_marion, 'outputs', 'SAM_states.csv'))
    # df_marion_SAMS = df_marion_SAMS[df_marion_SAMS['axis'] == 'MS']
    # df_marion_SAMS['t'] = df_marion_SAMS['t'] + delta_t_simuls
    #
    # # Organs
    # df_marion_organs = pd.read_csv(os.path.join(POSTPROCESSING_MARION, 'organs_postprocessing.csv'))
    # df_marion_organs = df_marion_organs[df_marion_organs['axis'] == 'MS']
    # df_marion_organs['t'] = df_marion_organs['t'] + delta_t_simuls
    #
    # # Elements
    # df_marion_elements = pd.read_csv(os.path.join(POSTPROCESSING_MARION, 'elements_postprocessing.csv'))
    # df_marion_elements = df_marion_elements[df_marion_elements['axis'] == 'MS']
    # df_marion_elements['t'] = df_marion_elements['t'] + delta_t_simuls
    #
    # # HZ
    # df_marion_hz = pd.read_csv(os.path.join(OUTPUTS_MARION, 'hiddenzones_states.csv'))
    # df_marion_hz = df_marion_hz[df_marion_hz['axis'] == 'MS']
    # df_marion_hz['t'] = df_marion_hz['t'] + delta_t_simuls

    tmin = df_current_axes.t.min()
    tmax = 4000#df_current_axes.t.max()

    # plot graphs
    with PdfPages('Comparison_scenarios.pdf') as pdf:
        # phloem
        phloem(df_scenarios_dict, tmin, tmax)

        # Photosynthesis
        photosynthesis(df_scenarios_dict)

        # roots
        roots(df_scenarios_dict, tmin, tmax)

        # dry mass & shoot : root
        dry_mass(df_scenarios_dict, tmin, tmax)

        # N mass
        N_mass(df_scenarios_dict, tmin, tmax)

        # Surfaces
        surface(df_scenarios_dict, tmin, tmax)

        # Final dimensions
        final_dimensions(df_scenarios_dict)
