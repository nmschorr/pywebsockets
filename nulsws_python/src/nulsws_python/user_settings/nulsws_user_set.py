#!/usr/bin/python3.7
"""
by Nancy Schorr for Nuls, None),
(December, None),
(2019

"""

# change user_settings to suit
# for use in api calls
# fill in your default params here
from configparser import ConfigParser


class NulsWsUserSet(object):

    def __init__(self):
        config = ConfigParser()
        myfile = "e:\\config.ini"
        config.read(myfile)
        clist = config.sections()

        d = {}
        for c in clist:
            d.update(c)

        my_minsigns, my_inputs, my_outputs, my_remark, my_signaddress = [1, 1, 1, 1, 1]

        z0_ADD_ADDRESS_PREFIX_prefix = d.my_addressprefix
        z1_AC_CREATE_ACCOUNT_chainId = d.my_chainid
        z1_AC_CREATE_ACCOUNT_count = d.my_chainid
        z1_AC_CREATE_ACCOUNT_password = d.my_password
        z2_AC_CREATE_CONTRACT_ACCOUNT_chainId = d.my_chainid
        z3_AC_CREATE_MULTI_SIGN_ACCOUNT_chainId = d.my_chainid
        z3_AC_CREATE_MULTI_SIGN_ACCOUNT_pubKeys = d.my_pubkeys
        z3_AC_CREATE_MULTI_SIGN_ACCOUNT_minSigns = d.my_minsigns
        z4_AC_CREATE_MULTI_SIGN_TRANSFER_chainId = d.my_chainid
        z4_AC_CREATE_MULTI_SIGN_TRANSFER_inputs = d.my_inputs
        z4_AC_CREATE_MULTI_SIGN_TRANSFER_outputs = d.my_outputs
        z4_AC_CREATE_MULTI_SIGN_TRANSFER_remark = d.my_remark
        z4_AC_CREATE_MULTI_SIGN_TRANSFER_signAddress = d.my_address
        z4_AC_CREATE_MULTI_SIGN_TRANSFER_signPassword = d.my_password
        z5_AC_CREATE_OFFLINE_ACCOUNT_chainId = d.my_chainid
        z5_AC_CREATE_OFFLINE_ACCOUNT_count = d.my_chainid
        z5_AC_CREATE_OFFLINE_ACCOUNT_password = d.my_chainid
        z6_AC_EXPORT_ACCOUNT_KEYSTORE_chainId = d.my_chainid
        z6_AC_EXPORT_ACCOUNT_KEYSTORE_address = d.my_address
        z6_AC_EXPORT_ACCOUNT_KEYSTORE_password = d.my_chainid
        z6_AC_EXPORT_ACCOUNT_KEYSTORE_filePath = d.my_chainid
        z7_AC_EXPORT_KEYSTORE_JSON_chainId = d.my_chainid
        z7_AC_EXPORT_KEYSTORE_JSON_address = d.my_address
        z7_AC_EXPORT_KEYSTORE_JSON_password = d.my_password
        z8_AC_GET_ACCOUNT_BYADDRESS_chainId = d.my_chainid
        z8_AC_GET_ACCOUNT_BYADDRESS_address = d.my_address
        z9_AC_GET_ACCOUNT_LIST_chainId = d.my_chainid
        z10_AC_GET_ADDRESS_LIST_chainId = d.my_chainid
        z10_AC_GET_ADDRESS_LIST_pageNumber = d.my_chainid
        z10_AC_GET_ADDRESS_LIST_pageSize = d.my_chainid
        z11_AC_GET_ADDRESS_PREFIX_BY_CHAINID_chainId = d.my_chainid
        z12_AC_GET_ALIASBY_ADDRESS_chainId = d.my_chainid
        z12_AC_GET_ALIASBY_ADDRESS_address = d.my_address
        z13_AC_GET_ALL_ADDRESS_PREFIX_chainId = d.my_chainid

        z14_AC_GET_ALL_PRIKEY_chainId = d.my_chainid

        z14_AC_GET_ALL_PRIKEY_password = d.my_password
        z15_AC_GET_ENCRYPTED_ADDRESS_LIST_chainId = d.my_chainid
        z16_AC_GET_MULTI_SIGN_ACCOUNT_chainId = d.my_chainid
        z16_AC_GET_MULTI_SIGN_ACCOUNT_address = d.my_address
        z17_AC_GET_PUBKEY_chainId = d.my_chainid
        z17_AC_GET_PUBKEY_address = d.my_address
        z17_AC_GET_PUBKEY_password = d.my_chainid
        z18_AC_IMPORT_ACCOUNT_BY_KEYSTORE_chainId = d.my_chainid
        z18_AC_IMPORT_ACCOUNT_BY_KEYSTORE_password = d.my_chainid
        z18_AC_IMPORT_ACCOUNT_BY_KEYSTORE_keyStore = d.my_chainid
        z18_AC_IMPORT_ACCOUNT_BY_KEYSTORE_overwrite = d.my_chainid
        z19_AC_IMPORT_ACCOUNT_BY_PRIKEY_chainId = d.my_chainid
        z19_AC_IMPORT_ACCOUNT_BY_PRIKEY_password = d.my_password
        z19_AC_IMPORT_ACCOUNT_BY_PRIKEY_priKey = d.my_chainid
        z19_AC_IMPORT_ACCOUNT_BY_PRIKEY_overwrite = d.my_chainid
        z20_AC_IS_ALIAS_USABLE_chainId = d.my_chainid
        z20_AC_IS_ALIAS_USABLE_alias = d.my_chainid
        z21_AC_IS_MULTISIGN_ACCOUNT_BUILDER_chainId = d.my_chainid
        z21_AC_IS_MULTISIGN_ACCOUNT_BUILDER_address = d.my_address
        z21_AC_IS_MULTISIGN_ACCOUNT_BUILDER_pubKey = d.my_chainid
        z22_AC_REMOVE_ACCOUNT_chainId = d.my_chainid
        z22_AC_REMOVE_ACCOUNT_address = d.my_address
        z22_AC_REMOVE_ACCOUNT_password = d.my_chainid
        z23_AC_REMOVE_MULTISIGN_ACCOUNT_chainId = d.my_chainid
        z23_AC_REMOVE_MULTISIGN_ACCOUNT_address = d.my_address
        z24_AC_SET_ALIAS_chainId = d.my_chainid
        z24_AC_SET_ALIAS_address = d.my_address
        z24_AC_SET_ALIAS_password = d.my_chainid
        z24_AC_SET_ALIAS_alias = d.my_chainid
        z25_AC_SET_MULTISIGN_ALIAS_chainId = d.my_chainid
        z25_AC_SET_MULTISIGN_ALIAS_address = d.my_address
        z25_AC_SET_MULTISIGN_ALIAS_alias = d.my_chainid
        z25_AC_SET_MULTISIGN_ALIAS_signAddress = d.my_address
        z25_AC_SET_MULTISIGN_ALIAS_signPassword = d.my_password
        z26_AC_SET_REMARK_chainId = d.my_chainid
        z26_AC_SET_REMARK_address = d.my_address
        z26_AC_SET_REMARK_remark = d.my_chainid
        z27_AC_SIGN_BLOCKDIGEST_chainId = d.my_chainid
        z27_AC_SIGN_BLOCKDIGEST_address = d.my_address
        z27_AC_SIGN_BLOCKDIGEST_password = d.my_chainid
        z27_AC_SIGN_BLOCKDIGEST_data = d.my_chainid
        z28_AC_SIGN_DIGEST_chainId = d.my_chainid
        z28_AC_SIGN_DIGEST_address = d.my_address
        z28_AC_SIGN_DIGEST_password = d.my_chainid
        z28_AC_SIGN_DIGEST_data = d.my_chainid
        z29_AC_SIGN_MULTISIGN_TRANSACTION_chainId = d.my_chainid
        z29_AC_SIGN_MULTISIGN_TRANSACTION_tx = d.my_chainid
        z29_AC_SIGN_MULTISIGN_TRANSACTION_signAddress = d.my_address
        z29_AC_SIGN_MULTISIGN_TRANSACTION_signPassword = d.my_password
        z30_AC_TRANSFER_chainId = d.my_chainid
        z30_AC_TRANSFER_inputs = d.my_chainid
        z30_AC_TRANSFER_outputs = d.my_chainid
        z30_AC_TRANSFER_remark = d.my_chainid
        z31_AC_UPDATE_OFFLINE_ACCOUNT_PASSWORD_chainId = d.my_chainid
        z31_AC_UPDATE_OFFLINE_ACCOUNT_PASSWORD_address = d.my_address
        z31_AC_UPDATE_OFFLINE_ACCOUNT_PASSWORD_password = d.my_chainid
        z31_AC_UPDATE_OFFLINE_ACCOUNT_PASSWORD_newPassword = d.my_chainid
        z31_AC_UPDATE_OFFLINE_ACCOUNT_PASSWORD_priKey = d.my_chainid
        z32_AC_UPDATE_PASSWORD_chainId = d.my_chainid
        z32_AC_UPDATE_PASSWORD_address = d.my_address
        z32_AC_UPDATE_PASSWORD_password = d.my_chainid
        z32_AC_UPDATE_PASSWORD_newPassword = d.my_chainid
        z33_AC_VALIDATION_PASSWORD_chainId = d.my_chainid
        z33_AC_VALIDATION_PASSWORD_address = d.my_address
        z33_AC_VALIDATION_PASSWORD_password = d.my_chainid
        z34_AC_VERIFY_SIGN_DATA_pubKey = d.my_chainid
        z34_AC_VERIFY_SIGN_DATA_sig = d.my_chainid
        z34_AC_VERIFY_SIGN_DATA_data = d.my_chainid
        z35_BATCH_VALIDATE_BEGIN_chainId = d.my_chainid
        z36_BLOCK_VALIDATE_chainId = d.my_chainid
        z36_BLOCK_VALIDATE_txList = d.my_chainid
        z38_CANCEL_CROSSCHAIN_chainId = d.my_chainid
        z38_CANCEL_CROSSCHAIN_assetId = d.my_chainid
        z39_CHECK_BLOCK_VERSION_chainId = d.my_chainid
        z39_CHECK_BLOCK_VERSION_extendsData = d.my_chainid
        z40_CM_ASSET_chainId = d.my_chainid
        z40_CM_ASSET_assetId = d.my_chainid
        z41_CM_ASSET_CIRCULATE_COMMIT_chainId = d.my_chainid
        z41_CM_ASSET_CIRCULATE_COMMIT_txList = d.my_chainid
        z41_CM_ASSET_CIRCULATE_COMMIT_blockHeader = d.my_chainid
        z42_CM_ASSET_CIRCULATE_ROLLBACK_chainId = d.my_chainid
        z42_CM_ASSET_CIRCULATE_ROLLBACK_txList = d.my_chainid
        z42_CM_ASSET_CIRCULATE_ROLLBACK_blockHeader = d.my_chainid
        z43_CM_ASSET_CIRCULATE_VALIDATOR_chainId = d.my_chainid
        z43_CM_ASSET_CIRCULATE_VALIDATOR_tx = d.my_chainid
        z44_CM_ASSET_DISABLE_chainId = d.my_chainid
        z44_CM_ASSET_DISABLE_assetId = d.my_chainid
        z44_CM_ASSET_DISABLE_address = d.my_address
        z44_CM_ASSET_DISABLE_password = d.my_password
        z45_CM_ASSET_REG_chainId = d.my_chainid
        z45_CM_ASSET_REG_assetId = d.my_chainid
        z45_CM_ASSET_REG_symbol = d.my_chainid
        z45_CM_ASSET_REG_assetName = d.my_chainid
        z45_CM_ASSET_REG_initNumber = d.my_chainid
        z45_CM_ASSET_REG_decimalPlaces = d.my_chainid
        z45_CM_ASSET_REG_address = d.my_address
        z45_CM_ASSET_REG_password = d.my_chainid
        z46_CM_CHAIN_chainId = d.my_chainid
        z47_CM_CHAIN_ACTIVE_chainId = d.my_chainid
        z47_CM_CHAIN_ACTIVE_chainName = d.my_chainid
        z47_CM_CHAIN_ACTIVE_addressType = d.my_address
        z47_CM_CHAIN_ACTIVE_addressPrefix = d.my_address
        z47_CM_CHAIN_ACTIVE_magicNumber = d.my_chainid
        z47_CM_CHAIN_ACTIVE_minAvailableNodeNum = d.my_chainid
        z47_CM_CHAIN_ACTIVE_assetId = d.my_chainid
        z47_CM_CHAIN_ACTIVE_symbol = d.my_chainid
        z47_CM_CHAIN_ACTIVE_assetName = d.my_chainid
        z47_CM_CHAIN_ACTIVE_initNumber = d.my_chainid
        z47_CM_CHAIN_ACTIVE_decimalPlaces = d.my_chainid
        z47_CM_CHAIN_ACTIVE_address = d.my_address
        z47_CM_CHAIN_ACTIVE_password = d.my_chainid
        z47_CM_CHAIN_ACTIVE_verifierList = d.my_chainid
        z47_CM_CHAIN_ACTIVE_signatureBFTRatio = d.my_chainid
        z47_CM_CHAIN_ACTIVE_maxSignatureCount = d.my_chainid
        z48_CM_CHAIN_REG_chainId = d.my_chainid
        z48_CM_CHAIN_REG_chainName = d.my_chainid
        z48_CM_CHAIN_REG_addressType = d.my_address
        z48_CM_CHAIN_REG_addressPrefix = d.my_address
        z48_CM_CHAIN_REG_magicNumber = d.my_chainid
        z48_CM_CHAIN_REG_minAvailableNodeNum = d.my_chainid
        z48_CM_CHAIN_REG_assetId = d.my_chainid
        z48_CM_CHAIN_REG_symbol = d.my_chainid
        z48_CM_CHAIN_REG_assetName = d.my_chainid
        z48_CM_CHAIN_REG_initNumber = d.my_chainid
        z48_CM_CHAIN_REG_decimalPlaces = d.my_chainid
        z48_CM_CHAIN_REG_address = d.my_address
        z48_CM_CHAIN_REG_password = d.my_chainid
        z48_CM_CHAIN_REG_verifierList = d.my_chainid
        z48_CM_CHAIN_REG_signatureBFTRatio = d.my_chainid
        z48_CM_CHAIN_REG_maxSignatureCount = d.my_chainid
        z49_CM_GET_CHAIN_ASSET_chainId = d.my_chainid
        z49_CM_GET_CHAIN_ASSET_assetChainId = d.my_chainid
        z49_CM_GET_CHAIN_ASSET_assetId = d.my_chainid
        z50_CM_GET_CIRCULATE_CHAIN_ASSET_circulateChainId = d.my_chainid
        z50_CM_GET_CIRCULATE_CHAIN_ASSET_assetChainId = d.my_chainid
        z50_CM_GET_CIRCULATE_CHAIN_ASSET_assetId = d.my_chainid
        z51_COMMIT_BATCH_UNCONFIRMED_TXS_chainId = d.my_chainid
        z51_COMMIT_BATCH_UNCONFIRMED_TXS_txList = d.my_chainid
        z52_COMMIT_BLOCKTXS_chainId = d.my_chainid
        z52_COMMIT_BLOCKTXS_txList = d.my_chainid
        z52_COMMIT_BLOCKTXS_blockHeight = d.my_chainid
        z53_COMMIT_UNCONFIRMEDTX_chainId = d.my_chainid
        z53_COMMIT_UNCONFIRMEDTX_tx = d.my_chainid
        z55_CREATE_AGENT_VALID_chainId = d.my_chainid
        z55_CREATE_AGENT_VALID_tx = d.my_chainid
        z56_CREATE_CROSSTX_chainId = d.my_chainid
        z56_CREATE_CROSSTX_listFrom = d.my_chainid
        z56_CREATE_CROSSTX_listTo = d.my_chainid
        z56_CREATE_CROSSTX_remark = d.my_chainid
        z57_CROSSCHAIN_REGISTER_CHANGE_chainId = d.my_chainid
        z58_CS_ADD_BLOCK_chainId = d.my_chainid
        z58_CS_ADD_BLOCK_blockHeader = d.my_chainid
        z59_CS_ADD_EVIDENCE_RECORD_chainId = d.my_chainid
        z59_CS_ADD_EVIDENCE_RECORD_blockHeader = d.my_chainid
        z59_CS_ADD_EVIDENCE_RECORD_evidenceHeader = d.my_chainid
        z60_CS_CHAIN_ROLLBACK_chainId = d.my_chainid
        z60_CS_CHAIN_ROLLBACK_height = d.my_chainid
        z61_CS_CONTRACT_DEPOSIT_chainId = d.my_chainid
        z61_CS_CONTRACT_DEPOSIT_agentHash = d.my_chainid
        z61_CS_CONTRACT_DEPOSIT_deposit = d.my_chainid
        z61_CS_CONTRACT_DEPOSIT_contractAddress = d.my_address
        z61_CS_CONTRACT_DEPOSIT_contractSender = d.my_chainid
        z61_CS_CONTRACT_DEPOSIT_contractBalance = d.my_chainid
        z61_CS_CONTRACT_DEPOSIT_contractNonce = d.my_chainid
        z61_CS_CONTRACT_DEPOSIT_blockTime = d.my_chainid
        z62_CS_CONTRACT_WITHDRAW_chainId = d.my_chainid
        z62_CS_CONTRACT_WITHDRAW_joinAgentHash = d.my_chainid
        z62_CS_CONTRACT_WITHDRAW_contractAddress = d.my_address
        z62_CS_CONTRACT_WITHDRAW_contractSender = d.my_chainid
        z62_CS_CONTRACT_WITHDRAW_contractBalance = d.my_chainid
        z62_CS_CONTRACT_WITHDRAW_contractNonce = d.my_chainid
        z62_CS_CONTRACT_WITHDRAW_blockTime = d.my_chainid
        z63_CS_CREATE_AGENT_chainId = d.my_chainid
        z63_CS_CREATE_AGENT_agentAddress = d.my_address
        z63_CS_CREATE_AGENT_packingAddress = d.my_address
        z63_CS_CREATE_AGENT_rewardAddress = d.my_address
        z63_CS_CREATE_AGENT_commissionRate = d.my_chainid
        z63_CS_CREATE_AGENT_deposit = d.my_chainid
        z63_CS_CREATE_AGENT_password = d.my_chainid
        z64_CS_CREATE_CONTRACT_AGENT_chainId = d.my_chainid
        z64_CS_CREATE_CONTRACT_AGENT_packingAddress = d.my_address
        z64_CS_CREATE_CONTRACT_AGENT_deposit = d.my_chainid
        z64_CS_CREATE_CONTRACT_AGENT_commissionRate = d.my_chainid
        z64_CS_CREATE_CONTRACT_AGENT_contractAddress = d.my_address
        z64_CS_CREATE_CONTRACT_AGENT_contractSender = d.my_chainid
        z64_CS_CREATE_CONTRACT_AGENT_contractBalance = d.my_chainid
        z64_CS_CREATE_CONTRACT_AGENT_contractNonce = d.my_chainid
        z64_CS_CREATE_CONTRACT_AGENT_blockTime = d.my_chainid
        z65_CS_CREATE_MULTI_AGENT_chainId = d.my_chainid
        z65_CS_CREATE_MULTI_AGENT_agentAddress = d.my_address
        z65_CS_CREATE_MULTI_AGENT_packingAddress = d.my_address
        z65_CS_CREATE_MULTI_AGENT_rewardAddress = d.my_address
        z65_CS_CREATE_MULTI_AGENT_commissionRate = d.my_chainid
        z65_CS_CREATE_MULTI_AGENT_deposit = d.my_chainid
        z65_CS_CREATE_MULTI_AGENT_password = d.my_chainid
        z65_CS_CREATE_MULTI_AGENT_signAddress = d.my_address
        z66_CS_DEPOSIT_TOAGENT_chainId = d.my_chainid
        z66_CS_DEPOSIT_TOAGENT_address = d.my_address
        z66_CS_DEPOSIT_TOAGENT_agentHash = d.my_chainid
        z66_CS_DEPOSIT_TOAGENT_deposit = d.my_chainid
        z66_CS_DEPOSIT_TOAGENT_password = d.my_chainid
        z67_CS_DOUBLE_SPEND_RECORD_chainId = d.my_chainid
        z67_CS_DOUBLE_SPEND_RECORD_block = d.my_chainid
        z67_CS_DOUBLE_SPEND_RECORD_tx = d.my_chainid
        z68_CS_GET_AGENT_ADDRESS_LIST_chainId = d.my_chainid
        z69_CS_GET_AGENT_CHANGE_INFO_chainId = d.my_chainid
        z70_CS_GET_AGENT_INFO_chainId = d.my_chainid
        z70_CS_GET_AGENT_INFO_agentHash = d.my_chainid
        z71_CS_GET_AGENT_LIST_chainId = d.my_chainid
        z71_CS_GET_AGENT_LIST_pageNumber = d.my_chainid
        z71_CS_GET_AGENT_LIST_pageSize = d.my_chainid
        z71_CS_GET_AGENT_LIST_keyWord = d.my_chainid
        z72_CS_GET_AGENT_STATUS_chainId = d.my_chainid
        z72_CS_GET_AGENT_STATUS_agentHash = d.my_chainid
        z73_CS_GET_CONSENSUS_CONFIG_chainId = d.my_chainid
        z74_CS_GET_CONTRACT_AGENT_INFO_chainId = d.my_chainid
        z74_CS_GET_CONTRACT_AGENT_INFO_agentHash = d.my_chainid
        z74_CS_GET_CONTRACT_AGENT_INFO_contractAddress = d.my_address
        z74_CS_GET_CONTRACT_AGENT_INFO_contractSender = d.my_chainid
        z75_CS_GET_CONTRACT_DEPOSIT_INFO_chainId = d.my_chainid
        z75_CS_GET_CONTRACT_DEPOSIT_INFO_joinAgentHash = d.my_chainid
        z75_CS_GET_CONTRACT_DEPOSIT_INFO_contractAddress = d.my_address
        z75_CS_GET_CONTRACT_DEPOSIT_INFO_contractSender = d.my_chainid
        z76_CS_GET_DEPOSIT_LIST_chainId = d.my_chainid
        z76_CS_GET_DEPOSIT_LIST_pageNumber = d.my_chainid
        z76_CS_GET_DEPOSIT_LIST_pageSize = d.my_chainid
        z76_CS_GET_DEPOSIT_LIST_address = d.my_address
        z76_CS_GET_DEPOSIT_LIST_agentHash = d.my_chainid
        z77_CS_GET_INFO_chainId = d.my_chainid
        z77_CS_GET_INFO_address = d.my_address
        z78_CS_GET_PACKER_INFO_chainId = d.my_chainid
        z79_CS_GET_PUBLISH_LIST_chainId = d.my_chainid
        z79_CS_GET_PUBLISH_LIST_address = d.my_address
        z79_CS_GET_PUBLISH_LIST_type = d.my_chainid
        z80_CS_GET_ROUND_INFO_chainId = d.my_chainid
        z81_CS_GET_ROUND_MEMBER_LIST_chainId = d.my_chainid
        z81_CS_GET_ROUND_MEMBER_LIST_extend = d.my_chainid
        z82_CS_GET_SEED_NODE_INFO_chainId = d.my_chainid
        z83_CS_GET_WHOLEINFO_chainId = d.my_chainid
        z84_CS_MULTI_DEPOSIT_chainId = d.my_chainid
        z84_CS_MULTI_DEPOSIT_address = d.my_address
        z84_CS_MULTI_DEPOSIT_agentHash = d.my_chainid
        z84_CS_MULTI_DEPOSIT_deposit = d.my_chainid
        z84_CS_MULTI_DEPOSIT_password = d.my_chainid
        z84_CS_MULTI_DEPOSIT_signAddress = d.my_address
        z85_CS_MULTI_WITHDRAW_chainId = d.my_chainid
        z85_CS_MULTI_WITHDRAW_address = d.my_address
        z85_CS_MULTI_WITHDRAW_txHash = d.my_chainid
        z85_CS_MULTI_WITHDRAW_password = d.my_chainid
        z85_CS_MULTI_WITHDRAW_signAddress = d.my_address
        z86_CS_RANDOM_RAW_SEEDS_COUNT_chainId = d.my_chainid
        z86_CS_RANDOM_RAW_SEEDS_COUNT_height = d.my_chainid
        z86_CS_RANDOM_RAW_SEEDS_COUNT_count = d.my_chainid
        z87_CS_RANDOM_RAW_SEEDS_HEIGHT_chainId = d.my_chainid
        z87_CS_RANDOM_RAW_SEEDS_HEIGHT_startHeight = d.my_chainid
        z87_CS_RANDOM_RAW_SEEDS_HEIGHT_endHeight = d.my_chainid
        z88_CS_RANDOM_SEED_COUNT_chainId = d.my_chainid
        z88_CS_RANDOM_SEED_COUNT_height = d.my_chainid
        z88_CS_RANDOM_SEED_COUNT_count = d.my_chainid
        z88_CS_RANDOM_SEED_COUNT_algorithm = d.my_chainid
        z89_CS_RANDOM_SEED_HEIGHT_chainId = d.my_chainid
        z89_CS_RANDOM_SEED_HEIGHT_startHeight = d.my_chainid
        z89_CS_RANDOM_SEED_HEIGHT_endHeight = d.my_chainid
        z89_CS_RANDOM_SEED_HEIGHT_algorithm = d.my_chainid
        z90_CS_RECEIVE_HEADERLIST_chainId = d.my_chainid
        z90_CS_RECEIVE_HEADERLIST_headerList = d.my_chainid
        z91_CS_RUN_CHAIN_chainId = d.my_chainid
        z92_CS_RUN_MAINCHAIN_chainId = d.my_chainid
        z93_CS_STOPAGENT_chainId = d.my_chainid
        z93_CS_STOPAGENT_address = d.my_address
        z93_CS_STOPAGENT_password = d.my_chainid
        z94_CS_STOP_AGENT_chainId = d.my_chainid
        z94_CS_STOP_AGENT_address = d.my_address
        z94_CS_STOP_AGENT_password = d.my_chainid
        z95_CS_STOPCHAIN_chainId = d.my_chainid
        z96_CS_STOP_CHAIN_chainId = d.my_chainid
        z97_CS_STOP_CONTRACT_AGENT_chainId = d.my_chainid
        z97_CS_STOP_CONTRACT_AGENT_contractAddress = d.my_address
        z97_CS_STOP_CONTRACT_AGENT_contractSender = d.my_chainid
        z97_CS_STOP_CONTRACT_AGENT_contractBalance = d.my_chainid
        z97_CS_STOP_CONTRACT_AGENT_contractNonce = d.my_chainid
        z97_CS_STOP_CONTRACT_AGENT_blockTime = d.my_chainid
        z98_CS_STOP_MULTI_AGENT_chainId = d.my_chainid
        z98_CS_STOP_MULTI_AGENT_address = d.my_address
        z98_CS_STOP_MULTI_AGENT_password = d.my_chainid
        z98_CS_STOP_MULTI_AGENT_signAddress = d.my_address
        z99_CS_TRIGGER_COINBASE_CONTRACT_chainId = d.my_chainid
        z99_CS_TRIGGER_COINBASE_CONTRACT_tx = d.my_chainid
        z99_CS_TRIGGER_COINBASE_CONTRACT_blockHeader = d.my_chainid
        z99_CS_TRIGGER_COINBASE_CONTRACT_stateRoot = d.my_chainid
        z100_CS_UPDATE_AGENT_CONSENSUS_STATUS_chainId = d.my_chainid
        z101_CS_UPDATE_AGENT_STATUS_chainId = d.my_chainid
        z101_CS_UPDATE_AGENT_STATUS_status = d.my_chainid
        z102_CS_VALIDBLOCK_chainId = d.my_chainid
        z102_CS_VALIDBLOCK_download = d.my_chainid
        z102_CS_VALIDBLOCK_block = d.my_chainid
        z103_CS_WITHDRAW_chainId = d.my_chainid
        z103_CS_WITHDRAW_address = d.my_address
        z103_CS_WITHDRAW_txHash = d.my_chainid
        z103_CS_WITHDRAW_password = d.my_chainid
        z104_DEPOSIT_VALID_chainId = d.my_chainid
        z104_DEPOSIT_VALID_tx = d.my_chainid
        z105_GET_ASSETS_BY_ID_chainId = d.my_chainid
        z105_GET_ASSETS_BY_ID_assetIds = d.my_chainid
        z106_GET_BALANCE_chainId = d.my_chainid
        z106_GET_BALANCE_assetChainId = d.my_chainid
        z106_GET_BALANCE_assetId = d.my_chainid
        z106_GET_BALANCE_address = d.my_address
        z107_GET_BALANCE_NONCE_chainId = d.my_chainid
        z107_GET_BALANCE_NONCE_assetChainId = d.my_chainid
        z107_GET_BALANCE_NONCE_assetId = d.my_chainid
        z107_GET_BALANCE_NONCE_address = d.my_address
        z107_GET_BALANCE_NONCE_isConfirmed = d.my_chainid
        z108_GET_BLOCK_BY_HASH_chainId = d.my_chainid
        z108_GET_BLOCK_BY_HASH_hash = d.my_chainid
        z109_GET_BLOCK_BY_HEIGHT_chainId = d.my_chainid
        z109_GET_BLOCK_BY_HEIGHT_height = d.my_chainid
        z110_GET_BLOCKHEADER_BY_HASH_chainId = d.my_chainid
        z110_GET_BLOCKHEADER_BY_HASH_hash = d.my_chainid
        z111_GET_BLOCKHEADER_BY_HEIGHT_chainId = d.my_chainid
        z111_GET_BLOCKHEADER_BY_HEIGHT_height = d.my_chainid
        z112_GET_BLOCKHEADER_PO_BY_HASH_chainId = d.my_chainid
        z112_GET_BLOCKHEADER_PO_BY_HASH_hash = d.my_chainid
        z113_GET_BLOCKHEADER_POBY_HEIGHT_chainId = d.my_chainid
        z113_GET_BLOCKHEADER_POBY_HEIGHT_height = d.my_chainid
        z114_GET_BLOCKHEADERS_BY_HEIGHT_RANGE_chainId = d.my_chainid
        z114_GET_BLOCKHEADERS_BY_HEIGHT_RANGE_begin = d.my_chainid
        z114_GET_BLOCKHEADERS_BY_HEIGHT_RANGE_end = d.my_chainid
        z115_GET_BLOCKHEADERS_FOR_PROTOCOL_chainId = d.my_chainid
        z115_GET_BLOCKHEADERS_FOR_PROTOCOL_interval = d.my_chainid
        z116_GET_BYZANTINE_COUNT_chainId = d.my_chainid
        z117_GET_CIRCULAT_chainId = d.my_chainid
        z117_GET_CIRCULAT_nodeId = d.my_chainid
        z117_GET_CIRCULAT_messageBody = d.my_chainid
        z119_GET_CROSSTX_STATE_chainId = d.my_chainid
        z119_GET_CROSSTX_STATE_txHash = d.my_chainid
        z120_GET_CTX_chainId = d.my_chainid
        z120_GET_CTX_nodeId = d.my_chainid
        z120_GET_CTX_messageBody = d.my_chainid
        z121_GET_CTX_STATE_chainId = d.my_chainid
        z121_GET_CTX_STATE_nodeId = d.my_chainid
        z121_GET_CTX_STATE_messageBody = d.my_chainid
        z122_GET_FRIEND_CHAIN_CIRCULATE_chainId = d.my_chainid
        z122_GET_FRIEND_CHAIN_CIRCULATE_assetIds = d.my_chainid
        z123_GET_LATEST_BLOCKHEADERS_chainId = d.my_chainid
        z123_GET_LATEST_BLOCKHEADERS_size = d.my_chainid
        z124_GET_LATEST_ROUND_BLOCKHEADERS_chainId = d.my_chainid
        z124_GET_LATEST_ROUND_BLOCKHEADERS_round = d.my_chainid
        z125_GET_NONCE_chainId = d.my_chainid
        z125_GET_NONCE_assetChainId = d.my_chainid
        z125_GET_NONCE_assetId = d.my_chainid
        z125_GET_NONCE_address = d.my_address
        z125_GET_NONCE_isConfirmed = d.my_chainid
        z126_GET_OTHERCTX_chainId = d.my_chainid
        z126_GET_OTHERCTX_nodeId = d.my_chainid
        z126_GET_OTHERCTX_messageBody = d.my_chainid
        z128_GET_ROUND_BLOCKHEADERS_chainId = d.my_chainid
        z128_GET_ROUND_BLOCKHEADERS_height = d.my_chainid
        z128_GET_ROUND_BLOCKHEADERS_round = d.my_chainid
        z129_GET_STATUS_chainId = d.my_chainid
        z130_GET_VERSION_chainId = d.my_chainid
        z131_INFO_chainId = d.my_chainid
        z132_LATEST_BLOCK_chainId = d.my_chainid
        z133_LATEST_BLOCKHEADER_chainId = d.my_chainid
        z134_LATEST_BLOCKHEADER_PO_chainId = d.my_chainid
        z135_LATEST_HEIGHT_chainId = d.my_chainid
        z137_MSG_PROCESS_chainId = d.my_chainid
        z137_MSG_PROCESS_nodeId = d.my_chainid
        z137_MSG_PROCESS_cmd = d.my_chainid
        z137_MSG_PROCESS_messageBody = d.my_chainid
        z138_NEW_BLOCK_HEIGHT_chainId = d.my_chainid
        z138_NEW_BLOCK_HEIGHT_height = d.my_chainid
        z139_NW_ACTIVE_CROSS_chainId = d.my_chainid
        z139_NW_ACTIVE_CROSS_maxOut = d.my_chainid
        z139_NW_ACTIVE_CROSS_maxIn = d.my_chainid
        z139_NW_ACTIVE_CROSS_seedIps = d.my_chainid
        z140_NW_ADD_NODES_chainId = d.my_chainid
        z140_NW_ADD_NODES_isCross = d.my_chainid
        z140_NW_ADD_NODES_nodes = d.my_chainid
        z141_NW_BROADCAST_chainId = d.my_chainid
        z141_NW_BROADCAST_excludeNodes = d.my_chainid
        z141_NW_BROADCAST_messageBody = d.my_chainid
        z141_NW_BROADCAST_command = d.my_chainid
        z141_NW_BROADCAST_isCross = d.my_chainid
        z141_NW_BROADCAST_percent = d.my_chainid
        z142_NW_CREATE_NODEGROUP_chainId = d.my_chainid
        z142_NW_CREATE_NODEGROUP_magicNumber = d.my_chainid
        z142_NW_CREATE_NODEGROUP_maxOut = d.my_chainid
        z142_NW_CREATE_NODEGROUP_maxIn = d.my_chainid
        z142_NW_CREATE_NODEGROUP_minAvailableCount = d.my_chainid
        z142_NW_CREATE_NODEGROUP_isCrossGroup = d.my_chainid
        z143_NW_DEL_NODES_chainId = d.my_chainid
        z143_NW_DEL_NODES_nodes = d.my_chainid
        z144_NW_GET_CHAIN_CONNECT_AMOUNT_chainId = d.my_chainid
        z144_NW_GET_CHAIN_CONNECT_AMOUNT_isCross = d.my_chainid
        z145_NW_GET_GROUP_BY_CHAINID_chainId = d.my_chainid
        z146_NW_GET_GROUPS_startPage = d.my_chainid
        z146_NW_GET_GROUPS_pageSize = d.my_chainid
        z147_NW_GET_NODES_chainId = d.my_chainid
        z147_NW_GET_NODES_state = d.my_chainid
        z147_NW_GET_NODES_isCross = d.my_chainid
        z147_NW_GET_NODES_startPage = d.my_chainid
        z147_NW_GET_NODES_pageSize = d.my_chainid
        z149_NW_INFO_chainId = d.my_chainid
        z150_NW_NODES_chainId = d.my_chainid
        z151_NW_PROTOCOL_REGISTER_role = d.my_chainid
        z151_NW_PROTOCOL_REGISTER_protocolCmds = d.my_chainid
        z152_NW_RECONNECT_chainId = d.my_chainid
        z153_NW_SEND_PEERS_MSG_chainId = d.my_chainid
        z153_NW_SEND_PEERS_MSG_nodes = d.my_chainid
        z153_NW_SEND_PEERS_MSG_messageBody = d.my_chainid
        z153_NW_SEND_PEERS_MSG_command = d.my_chainid
        z154_NW_UPDATE_NODE_INFO_chainId = d.my_chainid
        z154_NW_UPDATE_NODE_INFO_nodeId = d.my_chainid
        z154_NW_UPDATE_NODE_INFO_blockHeight = d.my_chainid
        z154_NW_UPDATE_NODE_INFO_blockHash = d.my_chainid
        z155_PARAM_TEST_CMD_intCount = d.my_chainid
        z155_PARAM_TEST_CMD_byteCount = d.my_chainid
        z155_PARAM_TEST_CMD_shortCount = d.my_chainid
        z155_PARAM_TEST_CMD_longCount = d.my_chainid
        z156_PROTOCOL_VERSION_CHANGE_chainId = d.my_chainid
        z156_PROTOCOL_VERSION_CHANGE_protocolVersion = d.my_chainid
        z157_RECEIVE_PACKING_BLOCK_chainId = d.my_chainid
        z157_RECEIVE_PACKING_BLOCK_block = d.my_chainid
        z158_RECV_CIRCULAT_chainId = d.my_chainid
        z158_RECV_CIRCULAT_nodeId = d.my_chainid
        z158_RECV_CIRCULAT_messageBody = d.my_chainid
        z159_RECV_CTX_chainId = d.my_chainid
        z159_RECV_CTX_nodeId = d.my_chainid
        z159_RECV_CTX_messageBody = d.my_chainid
        z160_RECV_CTX_HASH_chainId = d.my_chainid
        z160_RECV_CTX_HASH_nodeId = d.my_chainid
        z160_RECV_CTX_HASH_messageBody = d.my_chainid
        z161_RECV_CTX_SIGN_chainId = d.my_chainid
        z161_RECV_CTX_SIGN_nodeId = d.my_chainid
        z161_RECV_CTX_SIGN_messageBody = d.my_chainid
        z162_RECV_CTX_STATE_chainId = d.my_chainid
        z162_RECV_CTX_STATE_nodeId = d.my_chainid
        z162_RECV_CTX_STATE_messageBody = d.my_chainid
        z163_RECV_OTHER_CTX_chainId = d.my_chainid
        z163_RECV_OTHER_CTX_nodeId = d.my_chainid
        z163_RECV_OTHER_CTX_messageBody = d.my_chainid
        z164_RECV_REGCHAIN_chainId = d.my_chainid
        z164_RECV_REGCHAIN_nodeId = d.my_chainid
        z164_RECV_REGCHAIN_messageBody = d.my_chainid
        z166_REGISTER_PROTOCOL_chainId = d.my_chainid
        z166_REGISTER_PROTOCOL_moduleCode = d.my_chainid
        z166_REGISTER_PROTOCOL_list = d.my_chainid
        z167_ROLLBACK_BLOCK_TXS_chainId = d.my_chainid
        z167_ROLLBACK_BLOCK_TXS_txList = d.my_chainid
        z167_ROLLBACK_BLOCK_TXS_blockHeight = d.my_chainid
        z168_ROLLBACK_UNCONFIRM_TX_chainId = d.my_chainid
        z168_ROLLBACK_UNCONFIRM_TX_tx = d.my_chainid
        z169_ROLLBACK_BLOCK_chainId = d.my_chainid
        z169_ROLLBACK_BLOCK_blockHeader = d.my_chainid
        z170_ROLLBACK_TX_VALIDATE_STATUS_chainId = d.my_chainid
        z170_ROLLBACK_TX_VALIDATE_STATUS_tx = d.my_chainid
        z171_SAVE_BLOCK_chainId = d.my_chainid
        z171_SAVE_BLOCK_blockHeader = d.my_chainid
        z172_SC_BATCH_BEFORE_END_chainId = d.my_chainid
        z172_SC_BATCH_BEFORE_END_blockType = d.my_chainid
        z172_SC_BATCH_BEFORE_END_blockHeight = d.my_chainid
        z173_SC_BATCH_BEGIN_chainId = d.my_chainid
        z173_SC_BATCH_BEGIN_blockType = d.my_chainid
        z173_SC_BATCH_BEGIN_blockHeight = d.my_chainid
        z173_SC_BATCH_BEGIN_blockTime = d.my_chainid
        z173_SC_BATCH_BEGIN_packingAddress = d.my_address
        z173_SC_BATCH_BEGIN_preStateRoot = d.my_chainid
        z174_SC_BATCH_END_chainId = d.my_chainid
        z174_SC_BATCH_END_blockHeight = d.my_chainid
        z175_SC_CALL_chainId = d.my_chainid
        z175_SC_CALL_sender = d.my_chainid
        z175_SC_CALL_password = d.my_chainid
        z175_SC_CALL_value = d.my_chainid
        z175_SC_CALL_gasLimit = d.my_chainid
        z175_SC_CALL_price = d.my_chainid
        z175_SC_CALL_contractAddress = d.my_address
        z175_SC_CALL_methodName = d.my_chainid
        z175_SC_CALL_methodDesc = d.my_chainid
        z175_SC_CALL_args = d.my_chainid
        z175_SC_CALL_remark = d.my_chainid
        z176_SC_CALL_VALIDATOR_chainId = d.my_chainid
        z176_SC_CALL_VALIDATOR_tx = d.my_chainid
        z177_SC_CONSTRUCTOR_chainId = d.my_chainid
        z177_SC_CONSTRUCTOR_contractCode = d.my_chainid
        z178_SC_CONTRACT_INFO_chainId = d.my_chainid
        z178_SC_CONTRACT_INFO_contractAddress = d.my_address
        z179_SC_CONTRACT_OFFLINE_TX_HASH_LIST_chainId = d.my_chainid
        z179_SC_CONTRACT_OFFLINE_TX_HASH_LIST_blockHash = d.my_chainid
        z180_SC_CONTRACT_RESULT_chainId = d.my_chainid
        z180_SC_CONTRACT_RESULT_hash = d.my_chainid
        z181_SC_CONTRACT_RESULT_LIST_chainId = d.my_chainid
        z181_SC_CONTRACT_RESULT_LIST_hashList = d.my_chainid
        z182_SC_CONTRACT_TX_chainId = d.my_chainid
        z182_SC_CONTRACT_TX_hash = d.my_chainid
        z183_SC_CREATE_chainId = d.my_chainid
        z183_SC_CREATE_sender = d.my_chainid
        z183_SC_CREATE_password = d.my_chainid
        z183_SC_CREATE_alias = d.my_chainid
        z183_SC_CREATE_gasLimit = d.my_chainid
        z183_SC_CREATE_price = d.my_chainid
        z183_SC_CREATE_contractCode = d.my_chainid
        z183_SC_CREATE_args = d.my_chainid
        z183_SC_CREATE_remark = d.my_chainid
        z184_SC_CREATE_VALIDATOR_chainId = d.my_chainid
        z184_SC_CREATE_VALIDATOR_tx = d.my_chainid
        z185_SC_DELETE_chainId = d.my_chainid
        z185_SC_DELETE_sender = d.my_chainid
        z185_SC_DELETE_password = d.my_chainid
        z185_SC_DELETE_contractAddress = d.my_address
        z185_SC_DELETE_remark = d.my_chainid
        z186_SC_DELETE_VALIDATOR_chainId = d.my_chainid
        z186_SC_DELETE_VALIDATOR_tx = d.my_chainid
        z187_SC_IMPUTED_CALL_GAS_chainId = d.my_chainid
        z187_SC_IMPUTED_CALL_GAS_sender = d.my_chainid
        z187_SC_IMPUTED_CALL_GAS_value = d.my_chainid
        z187_SC_IMPUTED_CALL_GAS_contractAddress = d.my_address
        z187_SC_IMPUTED_CALL_GAS_methodName = d.my_chainid
        z187_SC_IMPUTED_CALL_GAS_methodDesc = d.my_chainid
        z187_SC_IMPUTED_CALL_GAS_args = d.my_chainid
        z188_SC_IMPUTED_CREATE_GAS_chainId = d.my_chainid
        z188_SC_IMPUTED_CREATE_GAS_sender = d.my_chainid
        z188_SC_IMPUTED_CREATE_GAS_contractCode = d.my_chainid
        z188_SC_IMPUTED_CREATE_GAS_args = d.my_chainid
        z189_SC_INITIAL_ACCOUNT_TOKEN_chainId = d.my_chainid
        z189_SC_INITIAL_ACCOUNT_TOKEN_address = d.my_address
        z190_SC_INVOKE_CONTRACT_chainId = d.my_chainid
        z190_SC_INVOKE_CONTRACT_blockType = d.my_chainid
        z190_SC_INVOKE_CONTRACT_tx = d.my_chainid
        z191_SC_INVOKE_VIEW_chainId = d.my_chainid
        z191_SC_INVOKE_VIEW_contractAddress = d.my_address
        z191_SC_INVOKE_VIEW_methodName = d.my_chainid
        z191_SC_INVOKE_VIEW_methodDesc = d.my_chainid
        z191_SC_INVOKE_VIEW_args = d.my_chainid
        z192_SC_PACKAGE_BATCH_END_chainId = d.my_chainid
        z192_SC_PACKAGE_BATCH_END_blockHeight = d.my_chainid
        z193_SC_TOKEN_ASSETS_LIST_chainId = d.my_chainid
        z193_SC_TOKEN_ASSETS_LIST_address = d.my_address
        z193_SC_TOKEN_ASSETS_LIST_pageNumber = d.my_chainid
        z193_SC_TOKEN_ASSETS_LIST_pageSize = d.my_chainid
        z194_SC_TOKEN_BALANCE_chainId = d.my_chainid
        z194_SC_TOKEN_BALANCE_contractAddress = d.my_address
        z194_SC_TOKEN_BALANCE_address = d.my_address
        z195_SC_TOKEN_TRANSFER_chainId = d.my_chainid
        z195_SC_TOKEN_TRANSFER_address = d.my_address
        z195_SC_TOKEN_TRANSFER_toAddress = d.my_address
        z195_SC_TOKEN_TRANSFER_contractAddress = d.my_address
        z195_SC_TOKEN_TRANSFER_password = d.my_chainid
        z195_SC_TOKEN_TRANSFER_amount = d.my_chainid
        z195_SC_TOKEN_TRANSFER_remark = d.my_chainid
        z196_SC_TOKEN_TRANSFER_LIST_chainId = d.my_chainid
        z196_SC_TOKEN_TRANSFER_LIST_address = d.my_address
        z196_SC_TOKEN_TRANSFER_LIST_pageNumber = d.my_chainid
        z196_SC_TOKEN_TRANSFER_LIST_pageSize = d.my_chainid
        z197_SC_TRANSFER_chainId = d.my_chainid
        z197_SC_TRANSFER_address = d.my_address
        z197_SC_TRANSFER_toAddress = d.my_address
        z197_SC_TRANSFER_password = d.my_chainid
        z197_SC_TRANSFER_amount = d.my_chainid
        z197_SC_TRANSFER_remark = d.my_chainid
        z198_SC_TRIGGER_PAYABLE_FOR_CONSENSUS_CONTRACT_chainId = d.my_chainid
        z198_SC_TRIGGER_PAYABLE_FOR_CONSENSUS_CONTRACT_stateRoot = d.my_chainid
        z198_SC_TRIGGER_PAYABLE_FOR_CONSENSUS_CONTRACT_blockHeight = d.my_chainid
        z198_SC_TRIGGER_PAYABLE_FOR_CONSENSUS_CONTRACT_contractAddress = d.my_address
        z198_SC_TRIGGER_PAYABLE_FOR_CONSENSUS_CONTRACT_tx = d.my_chainid
        z199_SC_UPLOAD_chainId = d.my_chainid
        z199_SC_UPLOAD_jarFileData = d.my_chainid
        z200_SC_VALIDATE_CALL_chainId = d.my_chainid
        z200_SC_VALIDATE_CALL_sender = d.my_chainid
        z200_SC_VALIDATE_CALL_value = d.my_chainid
        z200_SC_VALIDATE_CALL_gasLimit = d.my_chainid
        z200_SC_VALIDATE_CALL_price = d.my_chainid
        z200_SC_VALIDATE_CALL_contractAddress = d.my_address
        z200_SC_VALIDATE_CALL_methodName = d.my_chainid
        z200_SC_VALIDATE_CALL_methodDesc = d.my_chainid
        z200_SC_VALIDATE_CALL_args = d.my_chainid
        z201_SC_VALIDATE_CREATE_chainId = d.my_chainid
        z201_SC_VALIDATE_CREATE_sender = d.my_chainid
        z201_SC_VALIDATE_CREATE_gasLimit = d.my_chainid
        z201_SC_VALIDATE_CREATE_price = d.my_chainid
        z201_SC_VALIDATE_CREATE_contractCode = d.my_chainid
        z201_SC_VALIDATE_CREATE_args = d.my_chainid
        z202_SC_VALIDATE_DELETE_chainId = d.my_chainid
        z202_SC_VALIDATE_DELETE_contractAddress = d.my_address
        z203_STOP_AGENTVALID_chainId = d.my_chainid
        z203_STOP_AGENTVALID_tx = d.my_chainid
        z204_TX_COMMIT_chainId = d.my_chainid
        z204_TX_COMMIT_txList = d.my_chainid
        z204_TX_COMMIT_blockHeader = d.my_chainid
        z205_TX_VALIDATOR_chainId = d.my_chainid
        z205_TX_VALIDATOR_txList = d.my_chainid
        z205_TX_VALIDATOR_blockHeader = d.my_chainid
        z206_TX_BACK_PACKABLE_TXS_chainId = d.my_chainid
        z206_TX_BACK_PACKABLE_TXS_txList = d.my_chainid
        z207_TX_BATCH_VERIFY_chainId = d.my_chainid
        z207_TX_BATCH_VERIFY_txList = d.my_chainid
        z207_TX_BATCH_VERIFY_blockHeader = d.my_chainid
        z207_TX_BATCH_VERIFY_preStateRoot = d.my_chainid
        z208_TX_BL_STATE_chainId = d.my_chainid
        z208_TX_BL_STATE_status = d.my_chainid
        z209_TX_BLOCK_HEIGHT_chainId = d.my_chainid
        z209_TX_BLOCK_HEIGHT_height = d.my_chainid
        z210_TX_CS_STATE_chainId = d.my_chainid
        z210_TX_CS_STATE_packaging = d.my_chainid
        z211_TX_GET_BLOCKTXS_chainId = d.my_chainid
        z211_TX_GET_BLOCKTXS_txHashList = d.my_chainid
        z212_TX_GET_BLOCKTXS_EXTEND_chainId = d.my_chainid
        z212_TX_GET_BLOCKTXS_EXTEND_txHashList = d.my_chainid
        z212_TX_GET_BLOCKTXS_EXTEND_allHits = d.my_chainid
        z213_TX_GET_CONFIRMED_TX_chainId = d.my_chainid
        z213_TX_GET_CONFIRMED_TX_txHash = d.my_chainid
        z214_TX_GET_CONFIRMED_TX_CLIENT_chainId = d.my_chainid
        z214_TX_GET_CONFIRMED_TX_CLIENT_txHash = d.my_chainid
        z215_TX_GET_NONEXISTENT_UNCONFIRMED_HASHS_chainId = d.my_chainid
        z215_TX_GET_NONEXISTENT_UNCONFIRMED_HASHS_txHashList = d.my_chainid
        z216_TX_GET_SYSTEMTYPES_chainId = d.my_chainid
        z217_TX_GET_TX_chainId = d.my_chainid
        z217_TX_GET_TX_txHash = d.my_chainid
        z218_TX_GET_TX_CLIENT_chainId = d.my_chainid
        z218_TX_GET_TX_CLIENT_txHash = d.my_chainid
        z219_TX_NEWTX_chainId = d.my_chainid
        z219_TX_NEWTX_tx = d.my_chainid
        z220_TX_PACKABLE_TXS_chainId = d.my_chainid
        z220_TX_PACKABLE_TXS_endTimestamp = d.my_chainid
        z220_TX_PACKABLE_TXS_maxTxDataSize = d.my_chainid
        z220_TX_PACKABLE_TXS_blockTime = d.my_chainid
        z220_TX_PACKABLE_TXS_packingAddress = d.my_address
        z220_TX_PACKABLE_TXS_preStateRoot = d.my_chainid
        z221_TX_REGISTER_chainId = d.my_chainid
        z221_TX_REGISTER_moduleCode = d.my_chainid
        z221_TX_REGISTER_list = d.my_chainid
        z221_TX_REGISTER_delList = d.my_chainid
        z222_TX_ROLLBACK_chainId = d.my_chainid
        z222_TX_ROLLBACK_txHashList = d.my_chainid
        z222_TX_ROLLBACK_blockHeader = d.my_chainid
        z223_TX_SAVE_chainId = d.my_chainid
        z223_TX_SAVE_txList = d.my_chainid
        z223_TX_SAVE_contractList = d.my_chainid
        z223_TX_SAVE_blockHeader = d.my_chainid
        z224_TX_VERIFY_TX_chainId = d.my_chainid
        z224_TX_VERIFY_TX_tx = d.my_chainid
        z225_UPDATE_CHAIN_ASSET_chainId = d.my_chainid
        z225_UPDATE_CHAIN_ASSET_assets = d.my_chainid
        z226_VERIFY_COINDATA_chainId = d.my_chainid
        z226_VERIFY_COINDATA_tx = d.my_chainid
        z227_VERIFY_COINDATA_BATCH_PACKAGED_chainId = d.my_chainid
        z227_VERIFY_COINDATA_BATCH_PACKAGED_txList = d.my_chainid
        z228_WITHDRAW_VALID_chainId = d.my_chainid
        z228_WITHDRAW_VALID_tx = d.my_chainid

        # the following were added after the above numbers were created. The consist of 1000 + the
        # number that it should have been approximately

        z1017_AC_GET_PRIKEY_BY_ADDRESS__chainId = d.my_chainid
        z1017_AC_GET_PRIKEY_BY_ADDRESS_address = d.my_address
        z1017_AC_GET_PRIKEY_BY_ADDRESS_password = d.my_password
        return d
